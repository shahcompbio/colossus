# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-10 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190409_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='analysis',
            name='tenx_lanes',
            field=models.ManyToManyField(blank=True, to='core.TenxLane'),
        ),
    ]
