# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-13 17:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_userservicetoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='token',
            field=models.CharField(max_length=40),
        ),
    ]
