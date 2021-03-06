# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-21 22:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('location', models.TextField(default='Portland Gun Club')),
                ('started_at', models.CharField(choices=[('1', 'Station 1'), ('2', 'Station 2'), ('3', 'Station 3'), ('4', 'Station 4'), ('5', 'Station 5')], default='1', max_length=255)),
                ('excuses', models.TextField(default='')),
                ('score', models.CharField(blank=True, default='', max_length=25)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('sku', models.CharField(max_length=25)),
                ('shot', models.CharField(choices=[('7.5', '7.5 Shot'), ('8', '8 Shot'), ('8.5', '8.5'), ('9', '9')], default='7.5', max_length=255)),
                ('shot_amount', models.CharField(choices=[('7/8', '7/8oz'), ('1', '1oz'), ('1 1/8', '1 1/8oz')], default='1', max_length=255)),
                ('fps_rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shotgun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=25)),
                ('model', models.CharField(max_length=25)),
                ('barrel_length', models.IntegerField()),
                ('gauge', models.CharField(choices=[('12', '12 Gauge'), ('20', '20 Gauge'), ('28', '28 Gauge'), ('410', '410 Gauge')], default='12', max_length=255)),
                ('modifications', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='shells',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ammo', to='trap_scorekeeping.Shells'),
        ),
        migrations.AddField(
            model_name='round',
            name='shotgun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gun', to='trap_scorekeeping.Shotgun'),
        ),
    ]
