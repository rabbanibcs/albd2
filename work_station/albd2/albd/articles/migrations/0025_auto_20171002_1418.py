# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_auto_20171002_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.CharField(editable=False, max_length=500),
        ),
    ]
