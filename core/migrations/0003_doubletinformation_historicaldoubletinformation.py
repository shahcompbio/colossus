# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-07-15 21:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dlp', '0002_auto_20190712_1140'),
        ('core', '0002_auto_20190712_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubletInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of live single cells')),
                ('dead_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of dead single cells')),
                ('other_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of other single cells')),
                ('live_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of live doublet cells')),
                ('dead_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of dead doublet cells')),
                ('other_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of mixed doublet cells')),
                ('live_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two live cells')),
                ('dead_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two dead cells')),
                ('other_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two other cells')),
                ('library', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dlp.DlpLibrary', verbose_name='Library')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDoubletInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('live_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of live single cells')),
                ('dead_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of dead single cells')),
                ('other_single', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of other single cells')),
                ('live_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of live doublet cells')),
                ('dead_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of dead doublet cells')),
                ('other_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number of mixed doublet cells')),
                ('live_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two live cells')),
                ('dead_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two dead cells')),
                ('other_gt_doublet', models.IntegerField(blank=True, default=0, null=True, verbose_name='More than two other cells')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='dlp.DlpLibrary', verbose_name='Library')),
            ],
            options={
                'verbose_name': 'historical doublet information',
                'db_table': 'doublet_information_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
