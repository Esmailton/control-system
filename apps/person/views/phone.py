from django.views import generic
from apps.person.models import Phone
from django.urls import reverse_lazy
from ..forms import PhoneForm

class PhoneListView(generic.ListView):
    model = Phone
    paginate_by = 30
    queryset = Phone.objects.all()
    template_name = 'person/phone/phone_list.html'

class PhoneDetailView(generic.DetailView):
    model = Phone
    template_name = 'person/phone/phone_detail.html'
    form_class = PhoneForm

class PhoneCreateView(generic.CreateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy('person:phone_list')
    template_name = 'person/phone/phone_form.html'

class PhoneUpdateView(generic.UpdateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'person/phone/phone_form.html'

class PhoneDeleteView(generic.DeleteView):
    model = Phone
    success_url = reverse_lazy('person:phone_list')
    template_name = 'person/phone/phone_confirm_delete.html'