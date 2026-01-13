"""
URLs for PDF processor app
"""
from django.urls import path
from . import views

app_name = 'pdf_processor'

urlpatterns = [
    # Main upload endpoint
    path('upload/', views.upload_pdf, name='upload_pdf'),
    
    # Image endpoints
    path('images/', views.list_images, name='list_images'),
    path('extracted_images/<str:sid>/<str:filename>', views.extracted_image, name='extracted_image'),
    path('flip_image/<str:sid>/<str:filename>/<str:direction>', views.flip_image, name='flip_image'),
    
    # Progress endpoints (SSE)
    path('image_progress/', views.image_progress, name='image_progress'),
    path('alt_text_progress/', views.alt_text_progress, name='alt_text_progress'),
    
    # Alt text generation
    path('generate_alt_text/', views.generate_alt_text, name='generate_alt_text'),
    
    # Download and copy panel
    path('download_word/', views.download_word, name='download_word'),
    path('copy_panel/<str:sid>/', views.copy_panel, name='copy_panel'),
]

