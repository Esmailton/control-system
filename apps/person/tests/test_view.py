from django.test import TestCase
from django.urls import reverse
from uuid import uuid4
from ..models import Person

class PersonURLsTest(TestCase):

    def test_person_url(self):
        url_person = reverse('person:person')
        self.assertEqual(url_person, '/person/')

    def test_person_detail_url(self):
        person_id = uuid4()
        url_person_detail = reverse('person:person_detail', kwargs={'id': person_id})
        self.assertEqual(url_person_detail, f'/person/{person_id}/')

class PersonViewsTest(TestCase):

    def setUp(self):
        Person.objects.create(
            name='Foo Test',
            document='012.098.243-90'
        )
    
    def test_person_view_return_status_code_200(self):
        url = reverse('person:person')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_person_detail_view_return_status_code_200(self):
        person_id = Person.objects.all().first().id
        url_person_detail = reverse('person:person_detail', kwargs={'id': person_id})
        response = self.client.get(url_person_detail)
        self.assertEqual(response.status_code, 200)

    def test_person_view_render_correct_template(self):
        url = reverse('person:person')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'list_person.html')

    def test_person_detail_return_404(self):
        person_id = uuid4()
        url_person_detail = reverse('person:person_detail', kwargs={'id': person_id})
        response = self.client.get(url_person_detail)
        self.assertEqual(response.status_code, 404)

