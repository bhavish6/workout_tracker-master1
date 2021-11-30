# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0004_auto_20171105_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='workout.User'),
        ),
    ]
