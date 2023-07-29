from django.urls import path, include
from apps.core import views

app_name = 'core'

urlpatterns = [
    path('', views.Dashboad.as_view(), name='dashboard')
]   