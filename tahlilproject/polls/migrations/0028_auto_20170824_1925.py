# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 14:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0027_auto_20170824_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='id',
        ),
        migrations.AlterField(
            model_name='requestletter',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 24, 19, 25, 59, 481444), verbose_name='notification date'),
        ),
    ]
