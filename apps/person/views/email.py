from django.views import generic
from apps.person.models import Email
from django.urls import reverse_lazy
from ..forms import EmailForm


class EmailListView(generic.ListView):
    model = Email
    paginate_by = 30
    queryset = Email.objects.all()
    template_name = 'person/email/email_list.html'

class EmailDetailView(generic.DetailView):
    model = Email
    template_name = 'person/email/email_detail.html'

class EmailCreateView(generic.CreateView):
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('person:email_list')
    template_name = 'person/email/email_form.html'

class EmailUpdateView(generic.UpdateView):
    model = Email
    form_class = EmailForm
    template_name = 'person/email/email_form.html'

class EmailDeleteView(generic.DeleteView):
    model = Email
    success_url = reverse_lazy('person:email_list')
    template_name = 'person/email/email_confirm_delete.html'