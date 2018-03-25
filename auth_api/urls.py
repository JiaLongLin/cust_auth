#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from auth_api import views


urlpatterns = [
    url(r'^token/$', views.TokenView.as_view()),
    url(r'^refresh/$', views.RefreshTokenView.as_view()),
    url(r'^revoke/$', views.RevokeTokenView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
