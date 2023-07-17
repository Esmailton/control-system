from django.db import models
from apps.core.models import Base
from django.utils.translation import gettext_lazy as _
from django.db.models import UniqueConstraint
from apps.person.models import Person


class Country(Base, models.Model):
    name = models.CharField(_('Country'), max_length=100, unique=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countrys')

    def __str__(self):
        return self.name

class UF(Base, models.Model):
    name = models.CharField(_('State'), unique=True, max_length=50)
    acronym = models.CharField(_('Acronym'), unique=True, max_length=2)
    country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='country_uf', verbose_name=_('Country'))

    class Meta:
        verbose_name = _('UF')
        verbose_name_plural = _('UFs')
        constraints = [
            UniqueConstraint(
               "name",
               "acronym",
                name='unique_uf_name_acronym',
            ),
        ]


    def __str__(self):
        return f'{self.name}-{self.acronym}'

class City(Base, models.Model):
    name = models.CharField(_('City'), max_length=255, unique=True)
    uf = models.OneToOneField(UF, on_delete=models.CASCADE, related_name='uf_city', unique=True)

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Citys')
        constraints = [
            UniqueConstraint(
               "name",
               "uf",
                name='unique_uf_city',
            ),
        ]


class Address(Base, models.Model):
    logradouro = models.CharField(_('Logradouro'), max_length=255)
    number = models.IntegerField(_('Number'))
    zipcode = models.CharField(_('Zip Code'), blank=True, null=True, max_length=9)
    neighborhood = models.CharField(_('Neighborhood'), max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="person_address")

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Address')

    def __str__(self):
        return self.logradouro