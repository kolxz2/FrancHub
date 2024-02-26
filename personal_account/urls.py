from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
                  path('greeting/', my_view, name='greeting'),
                  path('create_franchise/', create_franchise, name='create_franchise'),
                  path('user_franchises/', user_franchises, name='user_franchises'),
                  path('user_buy_franchise_requests/', user_buy_franchise_requests, name='user_buy_franchise_requests'),
                  path('franchise/<int:franchise_id>/edit/', edit_franchise, name='edit_franchise'),
                  path('delete_franchise/', delete_franchise, name='delete_franchise'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
