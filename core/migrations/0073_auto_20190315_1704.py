# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-03-16 00:04
from __future__ import unicode_literals

import core.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20190315_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model, core.helpers.FieldValue),
        ),
        migrations.AddField(
            model_name='dlplibrary',
            name='projects',
            field=models.ManyToManyField(blank=True, to='core.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='pballibrary',
            name='projects',
            field=models.ManyToManyField(blank=True, to='core.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='tenxlibrary',
            name='projects',
            field=models.ManyToManyField(blank=True, to='core.Project', verbose_name='Project'),
        ),
        migrations.AddField(
            model_name='historicaltenxlibrary',
            name='google_sheet',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Google Sheet Link'),
        ),
        migrations.AddField(
            model_name='tenxlibrary',
            name='google_sheet',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Google Sheet Link'),
        ),
    ]