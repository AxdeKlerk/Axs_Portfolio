from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .error_probe import probe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path("probe/", probe),  # TEMPORARY!!
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)