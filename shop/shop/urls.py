from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include("product.urls")),
    path('', include("resources.urls")),
    path('', include("users.urls")),
    path('cart/', include("cart.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('en/', include('django.conf.urls.i18n')),
    path('', include('django.conf.urls.i18n')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
