from django.urls import path
from apps.person.views import (
        email_view, 
        person_view, 
        phone_view
    )

app_name = 'person'

urlpatterns = [
    path('person/list/', person_view.PersonListView.as_view(), name='person_list'),
    path('person/create/', person_view.PersonCreateView.as_view(), name='person_create'),
    path('person/detail/<uuid:pk>/', person_view.PersonDetailView.as_view(), name='person_detail'),
    path('person/update/<uuid:pk>/', person_view.PersonUpdateView.as_view(), name='person_update'),
    path('person/delete/<uuid:pk>/', person_view.PersonDeleteView.as_view(), name='person_delete'),

    path('email/list/', email_view.EmailListView.as_view(), name='email_list'),
    path('email/create/', email_view.EmailCreateView.as_view(), name='email_create'),
    path('email/detail/<uuid:pk>/', email_view.EmailDetailView.as_view(), name='email_detail'),
    path('email/update/<uuid:pk>/', email_view.EmailUpdateView.as_view(), name='email_update'),
    path('email/delete/<uuid:pk>/', email_view.EmailDeleteView.as_view(), name='email_delete'),

    path('phone/list/', phone_view.PhoneListView.as_view(), name='phone_list'),
    path('phone/create/', phone_view.PhoneCreateView.as_view(), name='phone_create'),
    path('phone/detail/<uuid:pk>/', phone_view.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/update/<uuid:pk>/', phone_view.PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/delete/<uuid:pk>/', phone_view.PhoneDeleteView.as_view(), name='phone_delete'),
]