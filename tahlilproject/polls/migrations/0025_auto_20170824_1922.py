# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20170824_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='id',
        ),
        migrations.AlterField(
            model_name='requestletter',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 19, 22, 29, 957673), verbose_name='notification date'),
        ),
    ]
