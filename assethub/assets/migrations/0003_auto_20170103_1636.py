# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('assets', '0002_auto_20170103_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=255)),
                ('notes', models.TextField(null=True)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=255)),
                ('notes', models.TextField(null=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assets.Application')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='asset',
            name='application',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='assets.Application'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asset',
            name='component',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='assets.Component'),
        ),
    ]
