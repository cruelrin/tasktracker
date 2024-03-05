
from django.conf import settings
from django.conf.urls.static import static

from tasktracker.views import base

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base, name='base'),
    path('tasktracker/', include('tasktracker.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
