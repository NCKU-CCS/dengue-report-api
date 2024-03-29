# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 16:34
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('bucket_id', models.TextField()),
                ('investigate_date', models.DateField()),
                ('county', models.TextField()),
                ('town', models.TextField()),
                ('village', models.TextField()),
                ('egg_count', models.IntegerField(default=0)),
                ('egypt_egg_count', models.IntegerField(default=0)),
                ('white_egg_count', models.IntegerField(default=0)),
                ('larvae_count', models.IntegerField(default=0)),
                ('egypt_larvae_count', models.IntegerField(default=0)),
                ('white_larvae_count', models.IntegerField(default=0)),
                ('note', models.TextField()),
            ],
        ),
    ]
