# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-12-12 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dlp', '0004_auto_20190917_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='dlpsequencing',
            name='external_gsc_id',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='External GSC ID'),
        ),
        migrations.AddField(
            model_name='historicaldlpsequencing',
            name='external_gsc_id',
            field=models.CharField(default=None, max_length=50, null=True, verbose_name='External GSC ID'),
        ),
    ]
