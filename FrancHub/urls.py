from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from FrancHub import settings
from FrancHub.view import redirect_view

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', redirect_view, name='redirect_view_name'),
                  path('', include('accounts.urls')),
                  path('', include('personal_account.urls')),
                  path('', include('buy_franchises.urls')),
                  path('', include('site_manager.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
