from django import forms
from .models import Category, Product, Service, MeasureType, Inventory
from django.contrib.admin.widgets import AutocompleteSelectMultiple, AutocompleteSelect
from django.contrib import admin


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price', 
            'picture', 
            'bar_code',
            'qr_code', 
            'internal_code', 
            'category', 
            'measuretype',
        ]

class ServiceForm(forms.ModelForm):
    product = forms.ModelMultipleChoiceField(
        queryset=Product.objects.all(),
        widget=AutocompleteSelectMultiple(Service._meta.get_field('product'), admin.site)
    )

    class Meta:
        model = Service
        fields = [
            'name',
            'description',
            'price',
            'picture',
            'product',
        ]

class MeasureTypeForm(forms.ModelForm):
    
    class Meta:
        model = MeasureType
        fields = [
                    'name', 
                    'description', 
                    'acronym', 
                    'measure_type'
                ]

class InventoryForm(forms.ModelForm):
    
    class Meta:
        model = Inventory
        fields = [
                    'product', 
                    'quantity', 
                    'reorder_point', 
                ]