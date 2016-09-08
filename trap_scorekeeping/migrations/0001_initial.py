# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-07 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gauge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gauge', models.CharField(choices=[(12, '12 Gauge'), (20, '20 Gauge'), (28, '28 Gauge'), (410, '410 Gauge')], default=12, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
                ('sku', models.TextField()),
                ('shot_weight', models.TextField()),
                ('shot_size', models.TextField()),
                ('dram_equivalent', models.TextField()),
                ('fps_rating', models.TextField()),
                ('gauge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shell_gauge', to='trap_scorekeeping.Gauge')),
            ],
        ),
        migrations.CreateModel(
            name='Shotgun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.TextField()),
                ('model', models.TextField()),
                ('barrel_length', models.TextField()),
                ('modifications', models.TextField()),
                ('gauge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shotgun_gauge', to='trap_scorekeeping.Gauge')),
            ],
        ),
        migrations.CreateModel(
            name='SinglesScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_type', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='shells',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trap_scorekeeping.Shells'),
        ),
    ]