from django.urls import path
from apps.person.views import email, person, phone
    
app_name = 'person'

urlpatterns = [
    path('person/list/', person.PersonListView.as_view(), name='person_list'),
    path('person/create/', person.PersonCreateView.as_view(), name='person_create'),
    path('person/detail/<uuid:pk>/', person.PersonDetailView.as_view(), name='person_detail'),
    path('person/update/<uuid:pk>/', person.PersonUpdateView.as_view(), name='person_update'),
    path('person/delete/<uuid:pk>/', person.PersonDeleteView.as_view(), name='person_delete'),

    path('email/list/', email.EmailListView.as_view(), name='email_list'),
    path('email/create/', email.EmailCreateView.as_view(), name='email_create'),
    path('email/detail/<uuid:pk>/', email.EmailDetailView.as_view(), name='email_detail'),
    path('email/update/<uuid:pk>/', email.EmailUpdateView.as_view(), name='email_update'),
    path('email/delete/<uuid:pk>/', email.EmailDeleteView.as_view(), name='email_delete'),

    path('phone/list/', phone.PhoneListView.as_view(), name='phone_list'),
    path('phone/create/', phone.PhoneCreateView.as_view(), name='phone_create'),
    path('phone/detail/<uuid:pk>/', phone.PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/update/<uuid:pk>/', phone.PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/delete/<uuid:pk>/', phone.PhoneDeleteView.as_view(), name='phone_delete'),
]