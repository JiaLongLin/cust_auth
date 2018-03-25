#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.db import models
from django.contrib.auth import get_user_model
from oauth2_provider.models import (
    AbstractGrant, AbstractRefreshToken,
    AbstractAccessToken, AbstractApplication
)


AUTH_USER_MODEL = get_user_model()


class Application(AbstractApplication):
    description = models.TextField()

    class Meta:
        pass

