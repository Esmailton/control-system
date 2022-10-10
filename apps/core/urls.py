from django.urls import include, path

from apps.core.views import home_page

urlpatterns = [
    path('', home_page),
    path('', include('apps.product.urls')),
]
