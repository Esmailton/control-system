from django.views import generic
from django.urls import reverse_lazy
from ..forms import MeasureTypeForm
from ..models import MeasureType

class MeasureTypeListView(generic.ListView):
    model = MeasureType
    paginate_by = 10
    queryset = MeasureType.objects.all()
    template_name = 'measure_type/measure_type_list.html'

class MeasureTypeCreateView(generic.CreateView):
    model = MeasureType
    form_class = MeasureTypeForm
    success_url = reverse_lazy('business:measure_type_list')
    queryset = MeasureType.objects.all()
    template_name = 'measure_type/measure_type_create.html'

class MeasureTypeUpdateView(generic.UpdateView):
    model = MeasureType
    form_class = MeasureTypeForm
    template_name = 'measure_type/measure_type_create.html'

class MeasureTypeDetailView(generic.DetailView):
    model = MeasureType
    template_name = 'measure_type/measure_type_detail.html'

class MeasureTypeDeleteView(generic.DeleteView):
    model = MeasureType
    success_url = reverse_lazy('person:measure_type_list')
    template_name = 'measure_type/measure_type_confirm_delete.html'