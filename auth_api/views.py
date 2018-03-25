#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from oauth2_provider.contrib.rest_framework.permissions import OAuth2Authentication

from auth_api import serializers


class TokenView(APIView):

    serializer_class = serializers.GenerateTokenSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            content = serializer.object
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(APIView):

    serializer_class = serializers.GenerateTokenSerializer
    authentication_classes = (OAuth2Authentication, )
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            content = serializer.object
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RevokeTokenView(APIView):

    authentication_classes = (OAuth2Authentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.RevokeTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            content = serializer.object
            return Response(content)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
