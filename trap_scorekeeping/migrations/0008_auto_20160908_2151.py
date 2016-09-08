# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-08 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trap_scorekeeping', '0007_auto_20160908_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShotAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_amount', models.CharField(choices=[('7/8', '7.5 Shot'), ('1', '8 Shot'), ('1 1/8', '8.5')], default='1', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ShotSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot', models.CharField(choices=[('7.5', '7.5 Shot'), ('8', '8 Shot'), ('8.5', '8.5'), ('9', '9')], default='7.5', max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='shells',
            name='dram_equivalent',
        ),
        migrations.AlterField(
            model_name='shells',
            name='brand',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='shells',
            name='fps_rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shells',
            name='shot_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='size', to='trap_scorekeeping.ShotSize'),
        ),
        migrations.AlterField(
            model_name='shells',
            name='shot_weight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weight', to='trap_scorekeeping.ShotAmount'),
        ),
        migrations.AlterField(
            model_name='shells',
            name='sku',
            field=models.CharField(max_length=25),
        ),
    ]
