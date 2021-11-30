# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='JoinUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full Name')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=10, verbose_name='Gender')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('mobile', models.CharField(max_length=13, verbose_name='Mobile')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('preference', models.CharField(max_length=10)),
                ('constituency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='joinus.Constituency')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='joinus.District')),
            ],
        ),
        migrations.AddField(
            model_name='constituency',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='constituencies', to='joinus.District'),
        ),
    ]
