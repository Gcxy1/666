# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-31 00:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shangpin',
            name='type',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
