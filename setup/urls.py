from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('apps.person.urls')),
    path('', include('apps.account.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.business.urls')),
]