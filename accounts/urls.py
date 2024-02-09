from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import register

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.LoginUser.as_view(), name='login_view'),
    path('logout/', views.logout_view,  name='logout'),
]
