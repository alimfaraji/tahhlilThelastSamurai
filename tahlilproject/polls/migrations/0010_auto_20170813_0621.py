# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-13 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20170813_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestletter',
            name='number',
        ),
        migrations.AddField(
            model_name='requestletter',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
