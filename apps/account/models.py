from apps.core.models import Base, Person
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserCustom(Base, AbstractUser):
    avatar = models.ImageField(upload_to=u"img/thumb/%Y/%m/%d", blank=True, null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person_of_user", blank=True, null=True, verbose_name=_('Pessoa') )
    is_admin = models.BooleanField(_('Administrator'),default=False)


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
