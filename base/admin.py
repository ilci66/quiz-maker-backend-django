from dataclasses import fields
from django.contrib import admin
# Register your models here.

# ------COPYING FROM BLOG POST AFTER HIS POINT------

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from .models import MyUser


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = {'email', 'date_of_birth', 'credits'}

    def clean_password2(self):
        password1 = self.changed_data.get("password1")
        password2 = self.changed_data.get("password2")
        if password1 and password2 and password2 != password1:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.changed_data["password1"])
        if commit:
            user.save()
        return user

    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth')}),
        ('Permissions', {'fields', ('is_admin',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'date_of_birth', 'password1', 'password2')
        })
    )
    search_fields = ('emails', )
    ordering = ('emails', )
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)