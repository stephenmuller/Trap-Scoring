# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trap_scorekeeping', '0006_auto_20160908_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='round',
            name='id',
        ),
        migrations.AlterField(
            model_name='round',
            name='singles_round',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='trap_scorekeeping.SinglesScore'),
        ),
    ]