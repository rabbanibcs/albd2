# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-10 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_banners', '0002_auto_20171110_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topbanner',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]