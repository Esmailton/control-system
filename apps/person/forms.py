from .models import Person, Email, Phone
from django import forms


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name','document','rg','birth_date']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email','person', 'type']

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone','person', 'type']