from django.urls import path

from .views import Category, Product

urlpatterns = [
    path('category/add/', Category.as_view(), name='category_view_add'),
    path('product/add/',  Product.as_view(), name='product_view_add'),
]
