# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-01 20:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def combine_sequencings(apps, schema_editor):
    DlpLibrary= apps.get_model('core', 'DlpLibrary')
    DlpSequencing = apps.get_model('core', 'DlpSequencing')

    for library in DlpLibrary.objects.all():
        if(library.dlpsequencing_set.filter(sequencing_center='BCCAGSC').count() >= 2):
            sequencings = library.dlpsequencing_set.filter(sequencing_center='BCCAGSC')
            base_sequencing = sequencings.first()

            for sequence in sequencings[1:]:
                for lane in sequence.dlplane_set.all():
                    lane.sequencing = base_sequencing
                    lane.save()
                sequence.delete()

        if(library.dlpsequencing_set.filter(sequencing_center='UBCBRC').count() >= 2):
            sequencings = library.dlpsequencing_set.filter(sequencing_center='UBCBRC')
            base_sequencing = sequencings.first()

            for sequence in sequencings[1:]:
                for lane in sequence.dlplane_set.all():
                    lane.sequencing = base_sequencing
                    lane.save()
                sequence.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20190125_1616'),
    ]

    operations = [
        migrations.RunPython(combine_sequencings),
    ]