from django.shortcuts import render
from django.views import View
from apps.person.models import Person
from django.shortcuts import get_object_or_404, get_list_or_404

# Create your views here.
class PersonView(View):

    def get(self, request, id=None):
        
        if id:
            person = get_object_or_404(Person,pk=id)
            return render(request, 'person_detail.html', context={
                'person': person
            })
        
        else:
            persons = get_list_or_404(Person)
            return render(request, 'list_person.html', context={
                'persons': persons
            })


    def post(self):
        ...

    def put(self):
        ...
        
    def delete(self):
        ...