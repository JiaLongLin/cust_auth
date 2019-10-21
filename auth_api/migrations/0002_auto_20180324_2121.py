# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-24 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myaccesstoken',
            name='application',
        ),
        migrations.RemoveField(
            model_name='myaccesstoken',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mygrant',
            name='application',
        ),
        migrations.RemoveField(
            model_name='mygrant',
            name='user',
        ),
        migrations.RemoveField(
            model_name='myrefreshtoken',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='myrefreshtoken',
            name='application',
        ),
        migrations.RemoveField(
            model_name='myrefreshtoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='MyAccessToken',
        ),
        migrations.DeleteModel(
            name='MyGrant',
        ),
        migrations.DeleteModel(
            name='MyRefreshToken',
        ),
    ]