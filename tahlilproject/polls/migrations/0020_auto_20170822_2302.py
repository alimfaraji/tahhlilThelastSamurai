# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 18:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_auto_20170822_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='polls.AvailableTimes'),
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='day',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time_partition',
        ),
        migrations.AlterUniqueTogether(
            name='reservation',
            unique_together=set([('neighbor', 'facility', 'time')]),
        ),
    ]