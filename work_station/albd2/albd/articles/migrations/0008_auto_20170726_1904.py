# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 13:04
from __future__ import unicode_literals

import autoslug.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20170726_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(allow_unicode=True, always_update=True, editable=False, max_length=1000, populate_from='title', unique_with=['publish_date__month', 'publish_date__day']),
        ),
    ]
