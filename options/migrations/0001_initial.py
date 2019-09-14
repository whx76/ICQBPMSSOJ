# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-17 09:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(db_index=True, unique=True)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]