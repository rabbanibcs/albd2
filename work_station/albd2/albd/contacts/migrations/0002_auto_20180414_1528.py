# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 09:28
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('recipients', django.db.models.manager.Manager()),
            ],
        ),
    ]
