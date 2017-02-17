# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.TextField()),
            ],
        ),
    ]
