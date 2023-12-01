from django.contrib import admin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import UniqueConstraint
from .models import Category, MeasureType, Product, Service, Inventory

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']

class MeasureTypeAdmin(admin.ModelAdmin):
    search_fields = ['name', 'acronym']

class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['category', 'measuretype']
    search_fields = ['name', 'category__name', 'measuretype__name']
    list_display = ['name', 'category', 'measuretype']

class ServiceAdmin(admin.ModelAdmin):
    filter_horizontal = ('product',)
    autocomplete_fields = ['product']
    search_fields = ['name', 'product__name']
    list_display = ['name']

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'reorder_point']

admin.site.register(Category, CategoryAdmin)
admin.site.register(MeasureType, MeasureTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Inventory, InventoryAdmin)
