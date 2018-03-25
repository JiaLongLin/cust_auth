#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, PermissionsMixin
from django.dispatch import receiver


@python_2_unicode_compatible
class MyUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **kwargs):
        if not username:
            raise ValueError(_('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(username, email, password, **kwargs)

    def create_superuser(self, username, email, password, **kwargs):
        kwargs.setdefault('is_admin', True)
        return self._create_user(username, email, password, **kwargs)


@python_2_unicode_compatible
class MyUserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, db_index=True)
    email = models.EmailField(max_length=200)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email', )

    class Meta:
        ordering = ('-created_at', )

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

    def is_superuser(self):
        return self.is_admin
