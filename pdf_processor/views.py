"""
Django views for PDF processing - converted from Flask app
"""
import os
import uuid
import json
import time
import logging
from pathlib import Path
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, StreamingHttpResponse, Http404
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

from .utils import (
    validate_session,
    sess_paths,
    ensure_dirs,
    write_progress,
    read_progress,
    write_status,
    read_status,
    read_alt_progress_detail,
    write_alt_progress_detail,
    read_json,
    write_json,
    start_extraction_async,
    background_generate_alt_text,
    _write_copy_panel_html,
    get_sessions_dir,
)

# Thread pool executor for background tasks
MAX_WORKERS = 1 if os.getenv("RENDER_DEBUG_SERIAL") == "1" else 4
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

# Ensure sessions directory exists
BASE_SESS = get_sessions_dir()
BASE_SESS.mkdir(exist_ok=True)


def reap_old_sessions(hours=6):
    """Delete session folders older than `hours` hours."""
    cutoff = time.time() - hours * 3600
    for child in BASE_SESS.iterdir():
        try:
            if child.is_dir() and child.stat().st_mtime < cutoff:
                import shutil
                shutil.rmtree(child, ignore_errors=True)
        except Exception:
            pass


# Run cleanup once at startup
reap_old_sessions()


@login_required
def index(request):
    """Main index page - same as accounts index but with PDF functionality."""
    return render(request, 'index.html')


@login_required
@ensure_csrf_cookie
@require_http_methods(["GET", "POST"])
def upload_pdf(request):
    """Handle PDF upload and start extraction."""
    if request.method == "POST":
        if "file" not in request.FILES:
            return JsonResponse({"success": False, "error": "No file part"}, status=400)

        file = request.FILES["file"]
        if not file or file.name == "":
            return JsonResponse({"success": False, "error": "No selected file"}, status=400)

        # Check file extension
        if not file.name.lower().endswith('.pdf'):
            return JsonResponse({"success": False, "error": "Only .pdf allowed"}, status=400)

        # Check file size (150 MB limit)
        if file.size > 150 * 1024 * 1024:
            return JsonResponse({
                "success": False,
                "error": "File size too large: Limit: 150MB. Please consider optimizing your file size or splitting your PDF file into separate parts.",
            }, status=413)

        # Generate session ID
        sid = str(uuid.uuid4())[:8]
        paths = sess_paths(sid)
        ensure_dirs(paths)

        # Save uploaded file
        filename = file.name
        pdf_path = paths["uploads"] / filename
        with open(pdf_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        # Initialize progress
        write_progress(paths["img_progress"], 0)
        write_status(paths["img_status"], "Queued…")

        # Start extraction in background
        executor.submit(start_extraction_async, str(pdf_path), paths)

        return JsonResponse({"success": True, "sid": sid, "images": []})

    return render(request, 'index.html', {"images": []})


@login_required
def extracted_image(request, sid, filename):
    """Serve extracted images."""
    if not validate_session(sid):
        logging.info(f"Invalid session ID in extracted_image: {sid}")
        return JsonResponse({"success": False, "error": "Invalid session ID"}, status=404)

    p = sess_paths(sid)
    file_path = (p["extracted"] / filename).resolve()
    
    if not file_path.is_file() or not str(file_path).startswith(str(p["extracted"].resolve())):
        return JsonResponse({"success": False, "error": "Invalid file path"}, status=404)

    from django.http import FileResponse
    return FileResponse(open(file_path, 'rb'), content_type='image/png')


@login_required
def flip_image(request, sid, filename, direction):
    """Flip an image horizontally or vertically."""
    if not validate_session(sid):
        logging.info(f"Invalid session ID in flip_image: {sid}")
        return JsonResponse({"success": False, "error": "Invalid session ID"}, status=404)

    p = sess_paths(sid)
    img_path = p["extracted"] / filename
    resolved_path = img_path.resolve()
    
    if not resolved_path.is_file() or not str(resolved_path).startswith(str(p["extracted"].resolve())):
        return JsonResponse({"success": False, "error": "Invalid file path"}, status=404)

    try:
        img = Image.open(str(img_path))
        if direction == "horizontal":
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif direction == "vertical":
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(str(img_path))
        return JsonResponse({"success": True})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


@login_required
@ensure_csrf_cookie
@require_http_methods(["POST"])
def generate_alt_text(request):
    """Start alt text generation."""
    try:
        data = json.loads(request.body)
        images = data.get("images", [])
        lang = data.get("lang", "en")
        sid = data.get("sid")
        
        if not sid:
            return JsonResponse({"success": False, "error": "Missing session id"}, status=400)
        if not images:
            return JsonResponse({"success": False, "error": "No images provided."}, status=400)

        executor.submit(background_generate_alt_text, images, lang, sid)
        return JsonResponse({"success": True, "session_id": sid})
    except Exception as e:
        logging.exception("generate_alt_text error")
        return JsonResponse({"success": False, "error": str(e)}, status=500)


@login_required
def download_word(request):
    """Download generated Word document."""
    lang = request.GET.get("lang", "en")
    sid = request.GET.get("id")
    
    if not sid:
        return HttpResponse("Missing session ID", status=400)

    p = sess_paths(sid)
    docx_path = p["output"] / f"alt_text_results_{sid}_{lang}.docx"
    ready_path = p["output"] / f"ready_{sid}_{lang}.txt"

    # Wait for file to be ready
    for _ in range(10):
        if docx_path.exists() and ready_path.exists():
            from django.http import FileResponse
            response = FileResponse(
                open(docx_path, 'rb'),
                content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            response['Content-Disposition'] = f'attachment; filename="{docx_path.name}"'
            
            # Cleanup after download
            def cleanup():
                try:
                    import shutil
                    shutil.rmtree(p["base"], ignore_errors=True)
                except Exception as e:
                    logging.info(f"⚠️ Cleanup after download failed: {e}")
            
            # Note: Django doesn't have call_on_close, so we'll handle cleanup differently
            # For now, we'll just return the file
            
            return response
        time.sleep(1)

    return HttpResponse("File not ready or failed to generate", status=500)


@login_required
def image_progress(request):
    """SSE endpoint for image extraction progress."""
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponse("Missing sid", status=400)
    
    p = sess_paths(sid)

    def generate():
        last_sent = None
        last_time = 0.0
        last_status = None
        base = sess_paths(sid)["base"]
        err_file = base / "error.txt"
        status_file = base / "status_image.txt"

        while True:
            progress = read_progress(p["img_progress"])
            status = read_status(status_file)

            # Send status changes
            if status and status != last_status:
                yield f"event: status\ndata: {status}\n\n"
                last_status = status

            now = time.time()
            if progress != last_sent or (now - last_time) > 5:
                yield f"data: {progress}\n\n"
                last_sent = progress
                last_time = now

            if progress >= 100:
                break
            if progress < 0:
                err_msg = "(unknown)"
                try:
                    if err_file.exists():
                        err_msg = (
                            err_file.read_text(encoding="utf-8")
                            .strip()
                            .replace("\n", " ")
                        )
                except Exception:
                    pass
                yield f"event: error\ndata: {err_msg}\n\n"
                break

            time.sleep(0.25)

    response = StreamingHttpResponse(
        generate(),
        content_type='text/event-stream'
    )
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    # Note: 'Connection: keep-alive' is a hop-by-hop header and cannot be set in WSGI
    return response


@login_required
def alt_text_progress(request):
    """SSE endpoint for alt text generation progress."""
    sid = request.GET.get("sid")
    if not sid:
        return HttpResponse("Missing sid", status=400)
    if not validate_session(sid):
        logging.info(f"Invalid session ID in alt_text_progress: {sid}")
        return HttpResponse("Invalid session ID", status=404)
    
    p = sess_paths(sid)

    def generate():
        last_payload = None
        while True:
            percent, done, total = read_alt_progress_detail(p["alt_progress"])
            payload = f"{percent}|{done}|{total}"
            if payload != last_payload:
                yield f"data: {payload}\n\n"
                last_payload = payload
            if percent >= 100:
                break
            time.sleep(0.3)

    response = StreamingHttpResponse(
        generate(),
        content_type='text/event-stream'
    )
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    # Note: 'Connection: keep-alive' is a hop-by-hop header and cannot be set in WSGI
    return response


@login_required
def list_images(request):
    """List extracted images for a session."""
    sid = request.GET.get("sid")
    if not sid:
        return JsonResponse({"success": False, "error": "Missing sid"}, status=400)
    if not validate_session(sid):
        logging.info(f"Invalid session ID in images: {sid}")
        return JsonResponse({"success": False, "error": "Invalid session ID"}, status=404)
    
    p = sess_paths(sid)
    j = p["base"] / "images.json"
    
    try:
        prog = read_progress(p["img_progress"])
        if j.exists():
            data = json.loads(j.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return JsonResponse({"success": True, "images": data})
        if prog < 100:
            return JsonResponse({"success": True, "images": []})
        extracted = p["extracted"]
        if extracted.exists():
            files = sorted(
                [
                    fn.name
                    for fn in extracted.iterdir()
                    if fn.is_file()
                    and fn.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
                ]
            )
            return JsonResponse({"success": True, "images": files})
        return JsonResponse({"success": True, "images": []})
    except Exception as e:
        return JsonResponse({"success": False, "error": f"/images failed: {e}"}, status=500)


@login_required
def copy_panel(request, sid):
    """Serve the copy panel HTML."""
    if not validate_session(sid):
        logging.info(f"Invalid session ID in copy_panel: {sid}")
        return HttpResponse("Invalid session ID", status=404)
    
    p = sess_paths(sid)
    path = p["output"] / f"copy_panel_{sid}.html"
    logging.info(f"Checking for copy panel: {path}")
    
    if not path.exists():
        logging.info(f"Copy panel not found: {path}")
        return HttpResponse("Not ready yet.", status=404)
    
    logging.info(f"Serving copy panel: {path}")
    from django.http import FileResponse
    return FileResponse(open(path, 'rb'), content_type='text/html')
