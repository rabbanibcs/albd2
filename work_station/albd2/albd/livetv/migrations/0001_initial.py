# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2021-02-16 06:56
from __future__ import unicode_literals

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0003_set_site_domain_and_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveTV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('embedded_link', models.URLField(blank=True, max_length=256, verbose_name='Embedded Link')),
                ('site', models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
