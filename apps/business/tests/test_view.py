from django.test import TestCase
from .business_test_base import FakeDataFactory
from django.urls import reverse
from uuid import uuid4
from ..models import Product, Category, MeasureType, Service


class ProductUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product = self.factory.create_product()

    def test_product_create_url(self):
        url_product = reverse('business:product_create')
        self.assertEqual(url_product, '/product/create/')

    def test_product_list_url(self):
        url_product = reverse('business:product_list')
        self.assertEqual(url_product, '/product/list/')

    def test_product_detail_url(self):
        product_id = uuid4()
        url_product_detail = reverse('business:product_detail', kwargs={'pk': product_id})
        self.assertEqual(url_product_detail, f'/product/detail/{product_id}/')
    
    def test_product_update_url(self):
        product_id = uuid4()
        url_product_update = reverse('business:product_update', kwargs={'pk': product_id})
        self.assertEqual(url_product_update, f'/product/update/{product_id}/')

    def test_product_delete_url(self):
        product_id = uuid4()
        url_product_update = reverse('business:product_delete', kwargs={'pk': product_id})
        self.assertEqual(url_product_update, f'/product/delete/{product_id}/')


class BusinessViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.product = self.factory.create_product()

    def test_product_view_return_status_code_200(self):
        url = reverse('business:product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_product_view_create_method_post_return_status_code_200(self):
        url = reverse('business:product_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_return_status_code_200(self):
        product_id = Product.objects.all().first().id
        url_product_detail = reverse('business:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url_product_detail)
        self.assertEqual(response.status_code, 200)

    def test_product_detail_view_render_correct_template(self):
        product_id = Product.objects.all().first().id
        url = reverse('business:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_detail.html')

    def test_product_view_create_render_correct_template(self):
        url = reverse('business:product_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_create.html')

    def test_product_view_update_render_correct_template(self):
        product= Product.objects.all().last()
        url = reverse('business:product_update', kwargs={'pk': product.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_create.html')

    def test_product_detail_return_404(self):
        product_id = uuid4()
        url_product_detail = reverse('business:product_detail', kwargs={'pk': product_id})
        response = self.client.get(url_product_detail)
        self.assertEqual(response.status_code, 404)


class CategorytUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.category = self.factory.create_category()

    def test_category_create_url(self):
        url_category = reverse('business:category_create')
        self.assertEqual(url_category, '/category/create/')

    def test_category_list_url(self):
        url_category = reverse('business:category_list')
        self.assertEqual(url_category, '/category/list/')

    def test_category_detail_url(self):
        category_id = uuid4()
        url_category_detail = reverse('business:category_detail', kwargs={'pk': category_id})
        self.assertEqual(url_category_detail, f'/category/detail/{category_id}/')
    
    def test_category_update_url(self):
        category_id = uuid4()
        url_category_update = reverse('business:category_update', kwargs={'pk': category_id})
        self.assertEqual(url_category_update, f'/category/update/{category_id}/')

    def test_category_delete_url(self):
        category_id = uuid4()
        url_category_update = reverse('business:category_delete', kwargs={'pk': category_id})
        self.assertEqual(url_category_update, f'/category/delete/{category_id}/')


class CategoryViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.category = self.factory.create_category()

    def test_category_view_return_status_code_200(self):
        url = reverse('business:category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_view_create_method_post_return_status_code_200(self):
        url = reverse('business:category_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_return_status_code_200(self):
        category_id = Category.objects.all().first().id
        url_category_detail = reverse('business:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url_category_detail)
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view_render_correct_template(self):
        category_id = Category.objects.all().first().id
        url = reverse('business:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_detail.html')

    def test_category_view_create_render_correct_template(self):
        url = reverse('business:category_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_create.html')

    def test_category_view_update_render_correct_template(self):
        category= Category.objects.all().last()
        url = reverse('business:category_update', kwargs={'pk': category.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'category/category_create.html')

    def test_category_detail_return_404(self):
        category_id = uuid4()
        url_category_detail = reverse('business:category_detail', kwargs={'pk': category_id})
        response = self.client.get(url_category_detail)
        self.assertEqual(response.status_code, 404)

class MeasureTypetUrlTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    def test_measure_type_create_url(self):
        url_measure_type = reverse('business:measure_type_create')
        self.assertEqual(url_measure_type, '/measure_type/create/')

    def test_measure_type_list_url(self):
        url_measure_type = reverse('business:measure_type_list')
        self.assertEqual(url_measure_type, '/measure_type/list/')

    def test_measure_type_detail_url(self):
        measure_type_id = uuid4()
        url_measure_type_detail = reverse('business:measure_type_detail', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_detail, f'/measure_type/detail/{measure_type_id}/')

    def test_measure_type_update_url(self):
        measure_type_id = uuid4()
        url_measure_type_update = reverse('business:measure_type_update', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_update, f'/measure_type/update/{measure_type_id}/')

    def test_measure_type_delete_url(self):
        measure_type_id = uuid4()
        url_measure_type_update = reverse('business:measure_type_delete', kwargs={'pk': measure_type_id})
        self.assertEqual(url_measure_type_update, f'/measure_type/delete/{measure_type_id}/')


class MeasureTypeViewsTest(TestCase):

    def setUp(self):
        self.factory= FakeDataFactory()
        self.measure_type = self.factory.create_measure_type()

    def test_measure_type_view_return_status_code_200(self):
        url = reverse('business:measure_type_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_view_create_method_post_return_status_code_200(self):
        url = reverse('business:measure_type_create')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_detail_view_return_status_code_200(self):
        measure_type_id = MeasureType.objects.all().first().id
        url_measure_type_detail = reverse('business:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url_measure_type_detail)
        self.assertEqual(response.status_code, 200)

    def test_measure_type_detail_view_render_correct_template(self):
        measure_type_id = MeasureType.objects.all().first().id
        url = reverse('business:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_detail.html')

    def test_measure_type_view_create_render_correct_template(self):
        url = reverse('business:measure_type_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_create.html')

    def test_measure_type_view_update_render_correct_template(self):
        measure_type= MeasureType.objects.all().last()
        url = reverse('business:measure_type_update', kwargs={'pk': measure_type.pk})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'measure_type/measure_type_create.html')

    def test_measure_type_detail_return_404(self):
        measure_type_id = uuid4()
        url_measure_type_detail = reverse('business:measure_type_detail', kwargs={'pk': measure_type_id})
        response = self.client.get(url_measure_type_detail)
        self.assertEqual(response.status_code, 404)

