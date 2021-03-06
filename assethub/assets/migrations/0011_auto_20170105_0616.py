# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 06:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0010_auto_20170104_1249'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('slug', models.SlugField(max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='license',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assets.License'),
        ),
    ]
