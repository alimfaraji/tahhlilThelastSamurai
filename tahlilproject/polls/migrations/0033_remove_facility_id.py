# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 08:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0032_auto_20170825_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='id',
        ),
    ]
