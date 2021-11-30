# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-17 15:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.image
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('categories', '0002_auto_20170717_1930'),
        ('positions', '0001_initial'),
        ('content_types', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_id', models.CharField(max_length=100, unique=True)),
                ('url', models.CharField(blank=True, max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('short_title', models.CharField(blank=True, max_length=150)),
                ('short_description', models.CharField(blank=True, max_length=1000)),
                ('description', models.TextField(blank=True)),
                ('core_issue', models.CharField(blank=True, max_length=1000)),
                ('seo_url', models.CharField(blank=True, max_length=200)),
                ('meta_key', models.CharField(blank=True, max_length=100)),
                ('meta_description', models.CharField(blank=True, max_length=1000)),
                ('lang', models.CharField(choices=[('English', 'en'), ('Bangla', 'bn')], max_length=10)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('courtesy', models.CharField(blank=True, max_length=200)),
                ('published', models.BooleanField(default=False)),
                ('draft', models.BooleanField(default=True)),
                ('created_by', models.IntegerField(editable=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('attachment', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attachment_article', to='filer.File')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content_types.ContentType')),
                ('detail_gfx', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail_gfx_article', to='filer.Image')),
                ('gfx', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gfx_article', to='filer.Image')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='positions.Position')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('vedio', filer.fields.file.FilerFileField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vedio_article', to='filer.File')),
            ],
        ),
    ]
