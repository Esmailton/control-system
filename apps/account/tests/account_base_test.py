from faker import Faker
from django.contrib.auth import get_user_model
from apps.person.models import Person


class FakeDataFactory:
    
    def __init__(self):
        self.fake = Faker()

    def create_user(self):
        username = self.fake.first_name()
        password = 'Fakepassword123*'
        person = Person.objects.create(name=self.fake.name())

        user = get_user_model()
        return user.objects.create(
            username = username,
            password=password,
            person = person,
            avatar = 'media/user/avatar/xpto.jpeg'
        )