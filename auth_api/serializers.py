#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import json
from urllib.parse import urlencode
from django.contrib.auth import get_user_model
from rest_framework import serializers
from oauthlib.oauth2.rfc6749.endpoints.pre_configured import Server, WebApplicationServer
# from oauth2_provider.oauth2_validators import OAuth2Validator
from auth_api.my_validators import MyAuth2Validator
from auth_api.models import MyApplication as Application
from oauth2_provider import models


AUTH_USER_MODEL = get_user_model()


class GenerateTokenSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(GenerateTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['client_id'] = serializers.CharField()
        self.fields['client_secret'] = serializers.CharField()
        self.fields['grant_type'] = serializers.ChoiceField(choices=[
            'password', 'client_credentials', 'authorization_code', 'openid', 'refresh_token'
        ])
        self.fields['username'] = serializers.CharField(required=False)
        self.fields['password'] = serializers.CharField(required=False)
        self.fields['code'] = serializers.CharField(required=False)
        self.fields['grant_type_for_scope'] = serializers.CharField(required=False)
        self.fields['claims'] = serializers.CharField(required=False)
        self.fields['refresh_token'] = serializers.CharField(required=False)
        self.fields['scopes'] = serializers.ListField(required=False)
        self.fields['code'] = serializers.CharField(required=False)
        self.fields['redirect'] = serializers.URLField(required=False)

    @property
    def object(self):
        return self.validated_data

    @staticmethod
    def create_token(client_id, client_secret, grant_type, username=None, password=None,
                     uri='/auth/token/', http_method='POST', **kwargs):
        extra_credentials = kwargs.get('extra_credentials', None)
        grant_type_for_scope = kwargs.get('grant_type_for_scope', None)
        claims = kwargs.get('claims', None)
        headers = kwargs.get('headers', dict())
        # scopes = kwargs.get('scopes', list())
        if grant_type == 'refresh_token':
            refresh_token = kwargs.get('refresh_token')
            params = {
                'refresh_token': refresh_token,
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': grant_type
            }
        elif grant_type == 'authorization_code':
            code = kwargs.get('code')
            redirect = kwargs.get('redirect')
            params = {
                'code': code,
                'client_id': client_id,
                'client_secret': client_secret,
                'grant_type': grant_type,
                'redirect': redirect
            }
        else:
            params = {
                'username': username,
                'password': password,
                'grant_type': grant_type,
                'client_id': client_id,
                'client_secret': client_secret,
                # 'scopes': scopes
            }
        body = urlencode(params)
        headers, content, status_code = Server(MyAuth2Validator()).create_token_response(
            uri, http_method, body, headers, extra_credentials, grant_type_for_scope, claims
        )
        content = json.loads(content)
        if 'access_token' in content:
            access_token = content['access_token']
            obj = models.AccessToken.objects.get(token=access_token)
            if not obj.user:
                obj.user = Application.objects.get(client_id=client_id).user
                obj.save()
        return headers, content, status_code

    def validate(self, attrs):
        headers, content, status_code = self.create_token(**attrs)
        return content

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class RevokeTokenSerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super(RevokeTokenSerializer, self).__init__(*args, **kwargs)
        self.fields['token'] = serializers.CharField()
        self.fields['client_id'] = serializers.CharField()
        self.fields['client_secret'] = serializers.CharField()

    @property
    def object(self):
        return self.validated_data

    def validate(self, attrs):
        headers = dict()
        http_method = 'POST'
        uri = '/auth/token/'
        body = urlencode(attrs)
        headers, content, status_code = Server(MyAuth2Validator()).create_revocation_response(
            uri, http_method, body, headers
        )
        if content == '':
            return dict()
        return json.loads(content)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
