# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-09 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenx', '0003_auto_20190507_0944'),
        ('dlp', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='tenxlibrary',
            name='relates_to_dlp',
            field=models.ManyToManyField(blank=True, to='dlp.DlpLibrary', verbose_name='Relates to (DLP)'),
        ),
    ]
