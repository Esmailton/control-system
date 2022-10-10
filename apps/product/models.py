
from django.db import models

from apps.core.models import Base, DateTimeModel


class Category(Base, DateTimeModel):
    category_name = models.CharField(max_length=50, verbose_name ='Nome da Categoria')

    def __str__(self):
        return self.category_name


class Product(Base, DateTimeModel):

    product_name = models.CharField(max_length=20, verbose_name ='Nome do Produto/Serviço')
    product_price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Valor do Produto/Serviço')
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    product_photo = models.ImageField(null=True, blank=True, upload_to='product', verbose_name='Foto do Produto')
    product_description = models.TextField(null=True, blank=True, verbose_name='Descrição do produto')
    product_bar_code = models.CharField(null=True, blank=True, max_length=100, verbose_name ='Codigo de Barras')

    def __str__(self):
        return self.product_name
        