# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_auto_20170822_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='availabletimes',
            old_name='time_partition',
            new_name='duration',
        ),
        migrations.AddField(
            model_name='availabletimes',
            name='hour',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='availabletimes',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
