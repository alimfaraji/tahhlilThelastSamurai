# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 13:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20170822_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestletter',
            name='date_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 8, 24, 17, 45, 57, 135990), null=True, verbose_name='notification date'),
        ),
    ]