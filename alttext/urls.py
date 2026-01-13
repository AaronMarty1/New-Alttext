from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth routes (login, logout, password reset)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Allauth routes (social authentication)
    path('accounts/', include('allauth.urls')),

    # PDF Processor routes
    path('pdf_processor/', include('pdf_processor.urls')),

    # App routes
    path('', include('accounts.urls')),
]
