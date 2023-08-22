from ..models import Person, Phone, Email
from faker import Faker

class FakeDataFactory:
    
    def __init__(self):
        self.fake = Faker()

    def create_person(self):
        name = self.fake.name()
        document = self.fake.random_number(digits=11)
        return Person.objects.create(name=name, document=document)

    def create_email(self):
        email = self.fake.email()
        person = self.create_person()
        return Email.objects.create(email=email, person=person, type="1")

    def create_phone(self):
        phone = str(self.fake.random_number(digits=11))
        person = self.create_person()
        return Phone.objects.create(phone=phone, person=person, type="1")

