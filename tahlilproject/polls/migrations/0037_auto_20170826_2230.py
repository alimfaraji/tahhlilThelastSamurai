# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0036_availabletimes_is_reserved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlypayment',
            name='payed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
