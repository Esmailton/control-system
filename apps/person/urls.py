from django.urls import path
from .views import PersonView

app_name = 'person'
urlpatterns = [
    path('person/', PersonView.as_view(), name='person'),
    path('person/<uuid:id>/', PersonView.as_view(), name='person_detail'),
]