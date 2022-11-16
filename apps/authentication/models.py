import uuid
from django.contrib.auth.models import (AbstractUser)
from django.db import models
from django.utils.translation import gettext as _


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    password = models.CharField(max_length=300, verbose_name=_('Senha'))
    avatar = models.ImageField(upload_to='user_avatar')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Data de Criação'))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_('Data de Modificação'))


    USERNAME_FIELD = 'username'
    USERNAME_FIELDS = ['username', 'password']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'