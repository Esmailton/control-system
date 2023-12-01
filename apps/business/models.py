from django.db import models
from apps.core.models import Base
from django.utils.translation import gettext_lazy as _
from django.db.models import UniqueConstraint
from django.urls import reverse


class Category(Base, models.Model):
    name = models.CharField(_('Name'), max_length=100)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['-create_at']
        constraints = [
            UniqueConstraint(
                    'name',
                    name='unique_name_category',
                )
            ]

    def get_absolute_url(self):
        return reverse("business:category_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class MeasureType(Base, models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(blank=True, null=True)
    acronym = models.CharField(_('acronym' ), max_length=4)
    measure_type = models.CharField(_('Measure Type'), max_length=100, blank=True, null=True)


    class Meta:
        verbose_name = _('Measure Type')
        verbose_name_plural = _('Measures Types')
        ordering = ['-create_at']
        constraints = [
            UniqueConstraint(
                'name',
                'acronym',
                name='unique_name_acronym_measure_type',
            )
        ]


    def get_absolute_url(self):
        return reverse("business:measure_type_detail", kwargs={"pk": self.id})
    
    def __str__(self):
        return self.name 


class Product(Base, models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(_('Description'),blank=True, null=True)
    price = models.DecimalField(_('Price'), max_digits=10, decimal_places=2)
    picture = models.ImageField(_('Picture'), upload_to=u"img/thumb/%Y/%m/%d", blank=True, null=True)
    bar_code = models.CharField(_('Bar Code'), max_length=255, null=True, blank=True)
    qr_code = models.CharField(_('Qr Code'), max_length=255, null=True, blank=True)
    internal_code = models.CharField(_('Internal Code'), max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, blank=True, null=True, related_name='product_category')
    measuretype = models.ForeignKey(MeasureType, on_delete=models.CASCADE, blank=True, null=True, related_name='product_measure')


    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['-create_at']
        constraints = [
            UniqueConstraint(
               'name',
               'category',
                name='unique_product_category_name',
            ),
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name='positive_price_constraint_product'
            )
        ]


    def get_absolute_url(self):
        return reverse("business:product_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Service(Base, models.Model):
    name = models.CharField(_('Name'), max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(_('Picture'), upload_to=u"img/thumb/%Y/%m/%d", blank=True, null=True)
    product = models.ManyToManyField(Product)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['-create_at']
        constraints = [
            models.CheckConstraint(
                check=models.Q(price__gte=0),
                name='positive_price_constraint_service'
            )
        ]

    def get_absolute_url(self):
        return reverse("business:service_detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Inventory(Base, models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='product_inventory')
    quantity = models.PositiveIntegerField(default=0)
    reorder_point = models.PositiveIntegerField(default=10)

    class Meta:
        verbose_name = _("inventory")
        verbose_name_plural = _("inventory")
        ordering = ['-create_at']

    def __str__(self):
        return f'{self.quantity}'
    
    def get_absolute_url(self):
        return reverse("business:inventory_detail", kwargs={"pk": self.pk})