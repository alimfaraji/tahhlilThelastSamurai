# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0030_auto_20170824_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestletter',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='name',
            field=models.CharField(max_length=20, primary_key=True),
        ),
    ]
