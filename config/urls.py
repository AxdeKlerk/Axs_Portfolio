from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .error_probe import probe, homepage_probe, home_debug

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path("probe/", probe),  # TEMPORARY!!
    path("probe-home/", homepage_probe),
    path("debug-home/", home_debug),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)