from django.urls import path
from apps.business import views

app_name = 'business'

urlpatterns = [
    path('product/list/', views.ProductListView.as_view(), name='product_list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('product/detail/<uuid:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/update/<uuid:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<uuid:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('category/list/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('category/detail/<uuid:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<uuid:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<uuid:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('service/list/', views.ServiceListView.as_view(), name='service_list'),
    path('service/create/', views.ServiceCreateView.as_view(), name='service_create'),
    path('service/detail/<uuid:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/update/<uuid:pk>/', views.ServiceUpdateView.as_view(), name='service_update'),
    path('service/delete/<uuid:pk>/', views.ServiceDeleteView.as_view(), name='service_delete'),

    path('measure_type/list/', views.MeasureTypeListView.as_view(), name='measure_type_list'),
    path('measure_type/create/', views.MeasureTypeCreateView.as_view(), name='measure_type_create'),
    path('measure_type/detail/<uuid:pk>/', views.MeasureTypeDetailView.as_view(), name='measure_type_detail'),
    path('measure_type/update/<uuid:pk>/', views.MeasureTypeUpdateView.as_view(), name='measure_type_update'),
    path('measure_type/delete/<uuid:pk>/', views.MeasureTypeDeleteView.as_view(), name='measure_type_delete'),

]
