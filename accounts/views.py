from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login
from .forms import SignupForm

class LoginView(BaseLoginView):
    """Custom login view that redirects authenticated users."""
    def dispatch(self, request, *args, **kwargs):
        # If user is already logged in, redirect to main page
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

def signup(request):
    # If user is already logged in, redirect to main page
    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# @login_required
# def dashboard(request):
#     return render(request, 'dashboard.html')
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
