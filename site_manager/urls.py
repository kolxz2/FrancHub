from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
                  path('franchise_validation/<int:franchise_id>/edit/', franchise_validation,
                       name='franchise_validation'),
                  path('all_site_franchises/', all_site_franchises, name='all_site_franchises'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
