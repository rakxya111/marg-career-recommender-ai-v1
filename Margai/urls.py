from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),
    path('ai/', include('margapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'marg/assets/img/favicon.ico')),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
