# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-25 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joinus', '0003_auto_20171125_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinus',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='joinus.Division'),
        ),
    ]