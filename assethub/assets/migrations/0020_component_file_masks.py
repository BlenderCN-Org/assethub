# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0019_auto_20170108_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='file_masks',
            field=models.CharField(default='*', max_length=64, verbose_name='Allowed file masks'),
        ),
    ]