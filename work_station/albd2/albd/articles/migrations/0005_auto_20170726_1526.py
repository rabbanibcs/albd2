# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-26 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import albd.articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20170726_1253'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish_date']},
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', albd.articles.models.ArticleManager()),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='url',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='short_description',
            new_name='snippet',
        ),
        migrations.AddField(
            model_name='article',
            name='allow_comments',
            field=models.BooleanField(default=True),
        ),
    ]
