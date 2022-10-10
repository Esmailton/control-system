from django.urls import path

from .views import Product

urlpatterns = [
    path('product/add/', Product.as_view(), name='category_view_add')
]
