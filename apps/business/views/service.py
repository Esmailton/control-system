from django.views import generic
from django.urls import reverse_lazy
from ..forms import ServiceForm
from ..models import Service

class ServiceListView(generic.ListView):
    model = Service
    paginate_by = 10
    queryset = Service.objects.all()
    template_name = 'service/service_list.html'

class ServiceCreateView(generic.CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('business:service_list')
    queryset = Service.objects.all()
    template_name = 'service/service_create.html'

class ServiceUpdateView(generic.UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'service/service_create.html'

class ServiceDetailView(generic.DetailView):
    model = Service
    template_name = 'service/service_detail.html'

class ServiceDeleteView(generic.DeleteView):
    model = Service
    success_url = reverse_lazy('person:service_list')
    template_name = 'service/service_confirm_delete.html'