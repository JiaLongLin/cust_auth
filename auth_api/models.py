#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch.dispatcher import receiver

from oauth2_provider.models import (
    AbstractAccessToken, AbstractApplication,
    AbstractRefreshToken, AbstractGrant
)

import redis

from server.settings import OAUTH2_PROVIDER

AUTHORIZATION_CODE_EXPIRE_SECONDS = OAUTH2_PROVIDER.get('AUTHORIZATION_CODE_EXPIRE_SECONDS', 60)
ACCESS_TOKEN_EXPIRE_SECONDS = OAUTH2_PROVIDER.get('ACCESS_TOKEN_EXPIRE_SECONDS', 3600)
REFRESH_TOKEN_EXPIRE_SECONDS = OAUTH2_PROVIDER.get('REFRESH_TOKEN_EXPIRE_SECONDS', 1440*60)

pool = redis.ConnectionPool(
    host='127.0.0.1',
    port=6379,
    password='Passw0rd'
)

redis_client = redis.StrictRedis(connection_pool=pool, db=2)

AUTH_USER_MODEL = get_user_model()


class MyApplication(AbstractApplication):
    description = models.CharField(max_length=200)
    scopes = models.TextField()

    class Meta:
        db_table = 'my_application'
        # managed = False


# class MyAccessToken(AbstractAccessToken):
#
#     user = models.ForeignKey(
#         AUTH_USER_MODEL, on_delete=models.CASCADE,
#         blank=True, null=True,
#         related_name="%(app_label)s_%(class)s"
#     )
#     application = models.ForeignKey(
#         MyApplication, on_delete=models.CASCADE,
#         blank=True, null=True,
#     )
#
#     @property
#     def scopes(self):
#         all_scopes = self.application.scopes.split()
#         token_scopes = self.scope.split()
#         return {name: None for name in all_scopes if name in token_scopes}
#
#     def allow_scopes(self, scopes):
#         if not scopes:
#             return True
#         provided_scopes = set(self.scope.split())
#         resource_scopes = set(scopes)
#
#         return resource_scopes.issubset(provided_scopes)
#
#     class Meta:
#         db_table = 'my_access_token'
#         # managed = False
#
#
# class MyRefreshToken(AbstractRefreshToken):
#     access_token = models.ForeignKey(MyAccessToken)
#     application = models.ForeignKey(MyApplication)
#
#     class Meta:
#         db_table = 'my_refresh_token'
#         # managed = False
#
#
# class MyGrant(AbstractGrant):
#
#     class Meta:
#         db_table = 'my_grant'
#         # managed = False
