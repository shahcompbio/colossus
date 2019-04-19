# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-18 21:06
from __future__ import unicode_literals

from django.db import migrations

from tenx.utils import tenxpool_naming_scheme


def update_pool_name(apps, shcema_editor):
    TenxPool = apps.get_model("core", "TenxPool")

    for pool in TenxPool.objects.all():
        pool.pool_name = tenxpool_naming_scheme(pool)
        pool.save()

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_tenxpool_pool_name'),
    ]

    operations = [
        migrations.RunPython(update_pool_name)
    ]
