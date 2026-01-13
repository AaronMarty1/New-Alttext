# from django.urls import path
# from accounts.views import index
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='dashboard'),
#     path('signup/', views.signup, name='signup'),
# ]
# urlpatterns = [
#     path('', index, name='index'),  # root now protected
# ]


from django.urls import path
from .views import signup, index, LoginView
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls')),   # 👈 ROOT goes through auth
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', signup, name='signup'),
    path('', index, name='index'),
]
