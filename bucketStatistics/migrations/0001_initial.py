# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-15 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketStatistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investigate_date', models.DateField()),
                ('county', models.TextField()),
                ('town', models.TextField()),
                ('village', models.TextField()),
                ('total_egg_count', models.IntegerField(default=0)),
                ('positive_rate', models.FloatField(default=0)),
            ],
        ),
    ]