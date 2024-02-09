from django.urls import path

from .views import my_view

urlpatterns = [
    path('greeting/', my_view, name='greeting'),
]