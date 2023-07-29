from apps.core.models import Base
from apps.person.models import Person
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .manager import UserManager



class UserCustom(Base, AbstractUser):
    avatar = models.ImageField(upload_to=u"img/thumb/%Y/%m/%d", blank=True, null=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="person_of_user", blank=True, null=True, verbose_name=_('Pessoa') )
    is_admin = models.BooleanField(_('Administrator'), default=False)

    objects = UserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS = ['is_admin', 'is_staff']

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username