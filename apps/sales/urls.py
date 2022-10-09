from django.urls import path

from apps.core.views import home_page

urlpatterns = [
    path('', home_page, name='home')
]
