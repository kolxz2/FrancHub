from django.urls import path

from . import views
from .views import login_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', views.logout_view,  name='logout'),
]
