# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_auto_20180902_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(default=2),
        ),
    ]