# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20170819_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='order',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
