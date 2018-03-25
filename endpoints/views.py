#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
from oauth2_provider.contrib.rest_framework.permissions import OAuth2Authentication, IsAuthenticatedOrTokenHasScope


class EndpointView(APIView):
    authentication_classes = (OAuth2Authentication, )
    permission_classes = (IsAuthenticatedOrTokenHasScope, )
    required_scopes = ['balabala']

    @staticmethod
    def get(request):
        return Response({'say': 'hello oauth.'})
