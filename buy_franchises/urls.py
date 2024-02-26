from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import main_list, franchise_info

urlpatterns = [
                  path('main_list/', main_list, name='main_list'),
                  path('franchise_info/<int:franchise_id>', franchise_info, name='franchise_info'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
