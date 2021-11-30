# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-14 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=13, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='designation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact_list', to='contacts.Designation'),
        ),
    ]
