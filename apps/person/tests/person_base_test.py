from django.test import TestCase
from ..models import Person


class PersonfactoryTest(TestCase):

    def person_factory(self):
        return Person.objects.create(
            name = "Foo",
            document = "123456789111"
        )