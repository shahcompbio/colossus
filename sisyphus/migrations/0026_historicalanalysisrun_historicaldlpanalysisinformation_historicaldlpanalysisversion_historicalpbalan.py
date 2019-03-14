# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-03-14 23:29
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0070_historicaladditionalsampleinformation_historicalchipregion_historicalchipregionmetadata_historicaldl'),
        ('sisyphus', '0025_tenxanalysisinformation_genome'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalAnalysisRun',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('last_updated', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Analysis last updated date/time')),
                ('run_status', models.CharField(choices=[('idle', 'Idle'), ('error', 'Error'), ('running', 'Running'), ('archiving', 'Archiving'), ('complete', 'Complete'), ('align_complete', 'Align Complete'), ('hmmcopy_complete', 'Hmmcopy Complete')], default='idle', max_length=50, verbose_name='Run Status')),
                ('log_file', models.CharField(blank=True, default=None, max_length=1000, null=True, verbose_name='error_log')),
                ('sftp_path', models.CharField(blank=True, max_length=50, null=True, verbose_name='sftp path')),
                ('blob_path', models.CharField(blank=True, max_length=50, null=True, verbose_name='Blob path')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'analysis_run_history',
                'verbose_name': 'historical analysis run',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDlpAnalysisInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('analysis_jira_ticket', models.CharField(max_length=50, null=True, verbose_name='Analysis Jira ticket')),
                ('priority_level', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=50, verbose_name='Priority Level')),
                ('aligner', models.CharField(choices=[('A', 'bwa-aln'), ('M', 'bwa-mem')], default='A', max_length=50, verbose_name='Aligner')),
                ('smoothing', models.CharField(choices=[('M', 'modal'), ('L', 'loess')], default='M', max_length=50, verbose_name='Smoothing')),
                ('analysis_submission_date', models.DateField(default=datetime.date.today, null=True, verbose_name='Analysis submission date')),
                ('verified', models.CharField(blank=True, choices=[('T', 'True'), ('F', 'False')], default='F', max_length=50, null=True, verbose_name='Verified')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('analysis_run', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.AnalysisRun')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.DlpLibrary', verbose_name='Library')),
                ('reference_genome', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.ReferenceGenome', verbose_name='ReferenceGenome')),
                ('version', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.DlpAnalysisVersion', verbose_name='Analysis Version')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'dlp_analysis_info_history',
                'verbose_name': 'historical dlp analysis information',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDlpAnalysisVersion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='DlpAnalysis Version')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'dlp_history_analysis_version',
                'verbose_name': 'historical dlp analysis version',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPbalAnalysisInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('analysis_jira_ticket', models.CharField(max_length=50, null=True, verbose_name='Analysis Jira ticket')),
                ('priority_level', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=50, verbose_name='Priority Level')),
                ('aligner', models.CharField(choices=[('A', 'bwa-aln'), ('M', 'bwa-mem')], default='A', max_length=50, verbose_name='Aligner')),
                ('smoothing', models.CharField(choices=[('M', 'modal'), ('L', 'loess')], default='M', max_length=50, verbose_name='Smoothing')),
                ('analysis_submission_date', models.DateField(default=datetime.date.today, null=True, verbose_name='Analysis submission date')),
                ('verified', models.CharField(blank=True, choices=[('T', 'True'), ('F', 'False')], default='F', max_length=50, null=True, verbose_name='Verified')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('analysis_run', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.AnalysisRun')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('reference_genome', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.ReferenceGenome', verbose_name='ReferenceGenome')),
                ('version', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.PbalAnalysisVersion', verbose_name='Analysis Version')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'pbal_analysis_info_history',
                'verbose_name': 'historical pbal analysis information',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPbalAnalysisVersion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='PbalAnalysis Version')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'pbal_history_analysis_version',
                'verbose_name': 'historical pbal analysis version',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReferenceGenome',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('reference_genome', models.CharField(max_length=50, verbose_name='reference_genome')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'ref_genome_history',
                'verbose_name': 'historical reference genome',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTenxAnalysisInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('analysis_jira_ticket', models.CharField(max_length=50, null=True, verbose_name='Analysis Jira ticket')),
                ('priority_level', models.CharField(choices=[('L', 'Low'), ('M', 'Medium'), ('H', 'High')], default='L', max_length=50, verbose_name='Priority Level')),
                ('aligner', models.CharField(choices=[('A', 'bwa-aln'), ('M', 'bwa-mem')], default='A', max_length=50, verbose_name='Aligner')),
                ('smoothing', models.CharField(choices=[('M', 'modal'), ('L', 'loess')], default='M', max_length=50, verbose_name='Smoothing')),
                ('analysis_submission_date', models.DateField(default=datetime.date.today, null=True, verbose_name='Analysis submission date')),
                ('verified', models.CharField(blank=True, choices=[('T', 'True'), ('F', 'False')], default='F', max_length=50, null=True, verbose_name='Verified')),
                ('genome', models.CharField(blank=True, max_length=50, null=True, verbose_name='Genome')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('analysis_run', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.AnalysisRun')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('reference_genome', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.ReferenceGenome', verbose_name='ReferenceGenome')),
                ('version', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sisyphus.TenxAnalysisVersion', verbose_name='Analysis Version')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'tenx_analysis_info_history',
                'verbose_name': 'historical tenx analysis information',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTenxAnalysisVersion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='TenxAnalysis Version')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'db_table': 'tenx_history_analysis_version',
                'verbose_name': 'historical tenx analysis version',
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
