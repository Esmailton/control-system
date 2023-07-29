from apps.account.models import UserCustom
from .form import UserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin


admin.site.register(UserCustom, UserAdmin)
admin.site.unregister(Group)