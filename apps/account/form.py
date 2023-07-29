from django import forms
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from apps.account.models import UserCustom

class UserCreationForm(forms.ModelForm):
    password=forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2=forms.CharField(
        label=_('Password confirmation'), widget=forms.PasswordInput
    )

    class Meta:
        model=UserCustom
        fields = '__all__'

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise ValidationError(_("Passwords must be the same!"))
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserCustom
        fields = "__all__"

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['username','person', 'date_joined', 'is_active', 'is_admin', 'is_staff','is_admin']
    list_filter =['is_admin', 'is_active']

    add_fieldsets =[
        (None, {"fields": ["username", "password", "password2"]}),
        ('Personal info', {'fields': ('person',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_admin')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ]

    search_fields = ["username"]
    ordering = ["username"]
    filter_horizontal =[]