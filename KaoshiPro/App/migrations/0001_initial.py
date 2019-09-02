# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-30 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shangpin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('impage', models.CharField(max_length=255)),
                ('price', models.FloatField(default=100.0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
