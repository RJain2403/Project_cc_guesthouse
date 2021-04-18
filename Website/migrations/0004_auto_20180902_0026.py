# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0003_auto_20180902_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='guesthouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Website.GuestHouse'),
        ),
    ]
