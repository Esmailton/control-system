from ..models import Category, MeasureType, Stock, Service, Product
from faker import Faker

class FakeDataFactory:
    
    def __init__(self):
        self.fake = Faker()

    def create_category(self):
        name = self.fake.word()
        return Category.objects.create(name=name)

    def create_measure_type(self):
        name = self.fake.word()
        description = self.fake.text()
        acronym = 'EX'
        measure_type = 'Peso'
        return MeasureType.objects.create(name=name, description=description, acronym=acronym, measure_type=measure_type)

    def create_product(self):

        # breakpoint()

        name = self.fake.word()
        description = self.fake.text()
        price = self.fake.random_int(min=1, max=100)
        picture = self.fake.file_path(depth=3)
        bar_code = self.fake.random_int(min=1, max=100)
        qr_code = self.fake.random_int(min=1, max=100)
        internal_code = self.fake.random_int(min=1, max=100)
        category= self.create_category()
        measuretype =self.create_measure_type()

        return Product.objects.create(
            name=name,
            description=description,
            price=price,
            picture=picture,
            bar_code=bar_code,
            qr_code=qr_code,
            internal_code=internal_code,
            category=category,
            measuretype=measuretype
        )

    def create_service(self):
        name = self.fake.word()
        description = self.fake.text()
        price = self.fake.random_int(min=1, max=10)
        picture = self.fake.file_path(depth=3)
        product = self.create_product()

        return Service.objects.create(
            name=name,
            description=description,
            price=price,
            picture=picture,
            product=product
        )