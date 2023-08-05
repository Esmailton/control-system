from django.views import generic
from apps.person.models import Person
from django.urls import reverse_lazy
from ..forms import PersonForm


class PersonListView(generic.ListView):
    model = Person
    paginate_by = 30
    queryset = Person.objects.all()

class PersonDetailView(generic.DetailView):
    model = Person

class PersonCreateView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url=reverse_lazy('person:person_list')

class PersonUpdateView(generic.UpdateView):
    model = Person
    form_class = PersonForm
    
class PersonDeleteView(generic.DeleteView):
    model = Person
    success_url=reverse_lazy('person:person_list')