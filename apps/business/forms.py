from django import forms
from .models import Category, Product, Service, MeasureType


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