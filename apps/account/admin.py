from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from apps.account.models import UserCustom

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2=forms.CharField(
        label=_('Password confirmation'), widget=forms.PasswordInput
    )

    class Meta:
        model=UserCustom
        fields = "__all__"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(_("Os passwords precisam ser iguais"))
        return password2
    
    
    
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserCustom
        fields = "__all__"

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['username','person', 'email', 'date_joined', 'is_active', 'is_admin', 'is_staff','is_admin']
    list_filter =['is_admin', 'is_active']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'avatar', 'person')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets =[
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2"],
            },
        ),
    ]

    search_fields = ["email", "username"]
    ordering = ["username"]
    filter_horizontal =[]

admin.site.register(UserCustom, UserAdmin)
admin.site.unregister(Group)