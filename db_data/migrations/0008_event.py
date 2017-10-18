# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2017-10-18 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_data', '0007_officer_tutor_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
