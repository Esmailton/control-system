from django.views import generic
from django.urls import reverse_lazy
from ..forms import InventoryForm
from ..models import Inventory

class InventoryListView(generic.ListView):
    model = Inventory
    paginate_by = 10
    queryset = Inventory.objects.select_related('product').all()
    template_name = 'inventory/inventory_list.html'

class InventoryCreateView(generic.CreateView):
    model = Inventory
    form_class = InventoryForm
    success_url = reverse_lazy('business:inventory_list')
    queryset = Inventory.objects.select_related('product').all()
    template_name = 'inventory/inventory_create.html'

class InventoryUpdateView(generic.UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_create.html'

class InventoryDetailView(generic.DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'

class InventoryDeleteView(generic.DeleteView):
    model = Inventory
    success_url = reverse_lazy('person:inventory_list')
    template_name = 'inventory/inventory_confirm_delete.html'