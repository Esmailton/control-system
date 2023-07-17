from django.test import TestCase
from django.urls import reverse
from uuid import uuid4
from ..models import Person
from .person_base_test import FakeDataFactory



class PersonUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.person = self.factory.create_person()

    def test_person_create_url(self):
        url_person = reverse('person:person_create')
        self.assertEqual(url_person, '/person/create/')

    def test_person_list_url(self):
        url_person = reverse('person:person_list')
        self.assertEqual(url_person, '/person/list/')

    def test_person_detail_url(self):
        person_id = uuid4()
        url_person_detail = reverse('person:person_detail', kwargs={'pk': person_id})
        self.assertEqual(url_person_detail, f'/person/detail/{person_id}/')
    
    def test_person_update_url(self):
        person_id = uuid4()
        url_person_update = reverse('person:person_update', kwargs={'pk': person_id})
        self.assertEqual(url_person_update, f'/person/update/{person_id}/')

    def test_person_delete_url(self):
        person_id = uuid4()
        url_person_update = reverse('person:person_delete', kwargs={'pk': person_id})
        self.assertEqual(url_person_update, f'/person/delete/{person_id}/')


class PersonViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.person = self.factory.create_person()

    def test_person_view_return_status_code_200(self):
        url = reverse('person:person_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_person_view_create_method_post_return_status_code_200(self):
        url = reverse('person:person_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_person_detail_view_return_status_code_200(self):
        person_id = Person.objects.all().first().id
        url_person_detail = reverse('person:person_detail', kwargs={'pk': person_id})
        response = self.client.get(url_person_detail)
        self.assertEqual(response.status_code, 200)

    def test_person_detail_view_render_correct_template(self):
        person_id = Person.objects.all().first().id
        url = reverse('person:person_detail', kwargs={'pk': person_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'person/person_detail.html')

    def test_person_view_create_render_correct_template(self):
        url = reverse('person:person_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'person/person_form.html')

    def test_person_view_update_render_correct_template(self):
        person= Person.objects.all().last()
        url = reverse('person:person_update', kwargs={'pk': person.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'person/person_form.html')

    def test_person_detail_return_404(self):
        person_id = uuid4()
        url_person_detail = reverse('person:person_detail', kwargs={'pk': person_id})
        response = self.client.get(url_person_detail)
        self.assertEqual(response.status_code, 404)


class PhoneUrlTest(TestCase):
    
    def setUp(self):
        self.factory = FakeDataFactory()
        self.phone = self.factory.create_phone()

    def test_phone_create_url(self):
        url_phones = reverse('person:phone_create')
        self.assertEqual(url_phones, '/phone/create/')

    def test_phone_list_url(self):
        url_phones = reverse('person:phone_list')
        self.assertEqual(url_phones, '/phone/list/')
        
    def test_phone_detail_url(self):
        phone_id = uuid4()
        url_phone_detail = reverse('person:phone_detail', kwargs={'pk': phone_id})
        self.assertEqual(url_phone_detail, f'/phone/detail/{phone_id}/')
    
    def test_phone_update_url(self):
        phone_id = uuid4()
        url_phone_detail = reverse('person:phone_update', kwargs={'pk': phone_id})
        self.assertEqual(url_phone_detail, f'/phone/update/{phone_id}/')

    def test_phone_delete_url(self):
        phone_id = uuid4()
        url_phone_detail = reverse('person:phone_delete', kwargs={'pk': phone_id})
        self.assertEqual(url_phone_detail, f'/phone/delete/{phone_id}/')

class PhoneViewsTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.phone = self.factory.create_phone()

    def test_phone_view_return_200(self):
        url = reverse('person:phone_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_phone_view_create_return_200(self):
        url = reverse('person:phone_create')
        person = Person.objects.all().last()
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_phone_view_update_return_200(self):
        url = reverse('person:phone_update', kwargs={'pk': self.phone.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_phone_view_delete_return_302(self):
        url = reverse('person:phone_delete', kwargs={'pk': self.phone.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)


class EmailUrlTest(TestCase):
    
    def setUp(self):
        self.factory = FakeDataFactory()
        self.email = self.factory.create_email()

    def test_email_create_url(self):
        url_emails = reverse('person:email_create')
        self.assertEqual(url_emails, '/email/create/')

    def test_email_list_url(self):
        url_emails = reverse('person:email_list')
        self.assertEqual(url_emails, '/email/list/')
        
    def test_email_detail_url(self):
        email_id = uuid4()
        url_email_detail = reverse('person:email_detail', kwargs={'pk': email_id})
        self.assertEqual(url_email_detail, f'/email/detail/{email_id}/')
    
    def test_email_update_url(self):
        email_id = uuid4()
        url_email_detail = reverse('person:email_update', kwargs={'pk': email_id})
        self.assertEqual(url_email_detail, f'/email/update/{email_id}/')

    def test_email_delete_url(self):
        email_id = uuid4()
        url_email_detail = reverse('person:email_delete', kwargs={'pk': email_id})
        self.assertEqual(url_email_detail, f'/email/delete/{email_id}/')


class EmailViewsTest(TestCase):

    def setUp(self):
        self.factory = FakeDataFactory()
        self.email = self.factory.create_email()

    def test_email_view_return_200(self):
        url = reverse('person:email_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_email_view_create_return_200(self):
        url = reverse('person:email_create')
        person = Person.objects.all().last()
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_email_view_update_return_200(self):
        url = reverse('person:email_update', kwargs={'pk': self.email.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_email_view_delete_return_302(self):
        url = reverse('person:email_delete', kwargs={'pk': self.email.pk})
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
