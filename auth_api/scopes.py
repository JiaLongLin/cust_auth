#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals


class BaseScopes(object):
    def get_all_scopes(self):
        """
        Return a dict-like object with all the scopes available in the
        system. The key should be the scope name and the value should be
        the description.

        ex: {"read": "A read scope", "write": "A write scope"}
        """
        raise NotImplementedError("")

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Return a list of scopes available for the current application/request.

        TODO: add info on where and why this method is called.

        ex: ["read", "write"]
        """
        raise NotImplementedError("")

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        """
        Return a list of the default scopes for the current application/request.
        This MUST be a subset of the scopes returned by `get_available_scopes`.

        TODO: add info on where and why this method is called.

        ex: ["read"]
        """
        raise NotImplementedError("")


class SettingsScopes(BaseScopes):
    def get_all_scopes(self):
        return {"read": "Reading scope", "write": "Writing scope"}

    def get_available_scopes(self, application=None, request=None, *args, **kwargs):
        return list()

    def get_default_scopes(self, application=None, request=None, *args, **kwargs):
        return list({"read": "Reading scope", "write": "Writing scope"}.keys())
