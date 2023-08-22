from django.urls import path
from apps.business.views import category, measure_type, service, product

app_name = 'business'

urlpatterns = [
    path('product/list/', product.ProductListView.as_view(), name='product_list'),
    path('product/create/', product.ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<uuid:pk>/', product.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<uuid:pk>/', product.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<uuid:pk>/', product.ProductDeleteView.as_view(), name='product_delete'),

    path('category/list/', category.CategoryListView.as_view(), name='category_list'),
    path('category/create/', category.CategoryCreateView.as_view(), name='category_create'),
    path('category/detail/<uuid:pk>/', category.CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<uuid:pk>/', category.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<uuid:pk>/', category.CategoryDeleteView.as_view(), name='category_delete'),

    path('service/list/', service.ServiceListView.as_view(), name='service_list'),
    path('service/create/', service.ServiceCreateView.as_view(), name='service_create'),
    path('service/detail/<uuid:pk>/', service.ServiceDetailView.as_view(), name='service_detail'),
    path('service/update/<uuid:pk>/', service.ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<uuid:pk>/', service.ServiceDeleteView.as_view(), name='service_delete'),

    path('measure_type/list/', measure_type.MeasureTypeListView.as_view(), name='measure_type_list'),
    path('measure_type/create/', measure_type.MeasureTypeCreateView.as_view(), name='measure_type_create'),
    path('measure_type/detail/<uuid:pk>/', measure_type.MeasureTypeDetailView.as_view(), name='measure_type_detail'),
    path('measure_type/update/<uuid:pk>/', measure_type.MeasureTypeUpdateView.as_view(), name='measure_type_update'),
    path('measure_type/delete/<uuid:pk>/', measure_type.MeasureTypeDeleteView.as_view(), name='measure_type_delete'),
]