# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-02 09:18
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0025_auto_20171002_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, always_update=True, editable=False, max_length=1000, populate_from='title', unique_with=['publish_date__month', 'publish_date__day', 'site', 'lang']),
        ),
    ]
