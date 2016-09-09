# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-09 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trap_scorekeeping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='first_position',
        ),
        migrations.AddField(
            model_name='round',
            name='started_at',
            field=models.CharField(choices=[('1', 'Station 1'), ('2', 'Station 2'), ('3', 'Station 3'), ('4', 'Station 4'), ('5', 'Station 5')], default='1', max_length=255),
        ),
        migrations.DeleteModel(
            name='Station',
        ),
    ]