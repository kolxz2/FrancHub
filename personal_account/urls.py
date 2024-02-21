from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
                  path('greeting/', my_view, name='greeting'),
                  path('create_franchise/', create_franchise, name='create_franchise'),
                  path('user_franchises/', user_franchises, name='user_franchises'),
                  path('franchise/<int:franchise_id>/edit/', edit_franchise, name='edit_franchise'),
                  # path('upload_photos/', upload_photos, name='upload_photos2'),
                  # path('photo_up/', upload_images, name='upload_photos'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
