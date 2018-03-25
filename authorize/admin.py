#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.contrib import admin
# from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from authorize.models import MyUserProfile


class UserCreateForm(UserCreationForm):
    class Meta:
        model = MyUserProfile
        fields = ('username', 'email')


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = MyUserProfile
        fields = ('username', 'email')


class MyUserAdmin(UserAdmin):

    form = MyUserChangeForm
    add_form = UserCreateForm

    list_display = ('username', 'created_at', 'email', 'is_delete', 'is_admin')
    search_fields = ('username', 'email')
    list_filter = ('is_admin',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'avatar',)}),
        ('Personal info', {'fields': ('created_at', 'updated_at')}),
        ('Permissions', {'fields': ('is_delete', 'is_admin', 'is_active')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            }
        ),
    )
    ordering = ('created_at',)
    filter_horizontal = ()


admin.site.register(MyUserProfile, MyUserAdmin)
