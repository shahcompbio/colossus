# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-05-07 16:44
from __future__ import unicode_literals

from django.db import migrations

from tenx.utils import tenxlibrary_naming_scheme


def format_tenxlibrary_naming(apps, schema_editor):
    tenx_library = apps.get_model('tenx', 'TenxLibrary')
    for library in tenx_library.objects.all():
        if not library.name.startswith('TENX'):
            library.name = tenxlibrary_naming_scheme(library)
        library.save()

class Migration(migrations.Migration):

    dependencies = [
        ('tenx', '0002_auto_20190506_1410'),
    ]

    operations = [
        migrations.RunPython(format_tenxlibrary_naming),
    ]