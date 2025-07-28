from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def media_serve(request, path):
    return serve(request, path, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', include('it_agri_app.urls')),  # Public-facing URLs (home, about, services)
    path('', include('admin_panel_app.urls')),  # Custom admin URLs (admin/login/, admin/dashboard/)
    path('admin/', admin.site.urls),  # Default Django admin
] 

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', media_serve),
        
    ]