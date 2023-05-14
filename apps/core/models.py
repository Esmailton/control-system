import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Person(models.Model):
    name = models.CharField(_('Nome Completo'), max_length=255)
    document = models.CharField(_('Documento CPF/CNPJ'), max_length=255)


    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')


    def __str__(self):
        return self.name