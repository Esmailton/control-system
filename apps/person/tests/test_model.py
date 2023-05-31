from django.test import TestCase
from django.core.exceptions import ValidationError
from .person_base_test import PersonfactoryTest
from parameterized import parameterized

from ..models import Person

class PersonModelTest(PersonfactoryTest):
    
    def setUp(self) -> None:
        self.person = self.person_factory()
        return super().setUp()

    @parameterized.expand([
            ('name', 100),    
            ('document', 14),
        ])
    def test_person_fields_max_length(self, field,max_length):
        setattr(self.person, field, 'X' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.person.full_clean()
