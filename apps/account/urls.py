from django.urls import path, include

app_name = 'account'

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls"))
]