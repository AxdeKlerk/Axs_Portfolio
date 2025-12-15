from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import custom_404, custom_500, force_500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    path("force-500/", force_500),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
