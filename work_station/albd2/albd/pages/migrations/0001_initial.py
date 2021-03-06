# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-18 07:10
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import albd.pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0003_set_site_domain_and_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('menu_label', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(allow_unicode=True, always_update=True, blank=True, editable=False, max_length=100, populate_from='name', unique_with=['name'])),
                ('body', models.TextField(blank=True)),
                ('published_date', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Pages',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', albd.pages.models.PageManager()),
            ],
        ),
    ]
