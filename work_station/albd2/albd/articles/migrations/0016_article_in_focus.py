# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-19 20:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20170818_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='in_focus',
            field=models.BooleanField(default=False, verbose_name='Show in Focus'),
        ),
    ]
