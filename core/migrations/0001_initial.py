# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-07-12 18:40
from __future__ import unicode_literals

import core.helpers
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalSampleInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tissue_state', models.CharField(blank=True, choices=[('NONE', 'None'), ('FROZ', 'Frozen'), ('FRES', 'Fresh'), ('DIG-FRES', 'Digested-Fresh')], default='NONE', max_length=50, null=True, verbose_name='Tissue State')),
                ('cancer_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cancer Type')),
                ('cancer_subtype', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cancer Subtype')),
                ('disease_condition_health_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Disease condition/health status')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Mixed'), ('U', 'Unknown')], max_length=50, null=True, verbose_name='Sex')),
                ('patient_biopsy_date', models.DateField(blank=True, null=True, verbose_name='Patient biopsy date')),
                ('anatomic_site', models.CharField(max_length=50, null=True, verbose_name='Anatomic site')),
                ('anatomic_sub_site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Anatomic sub-site')),
                ('developmental_stage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Developmental stage')),
                ('tissue_type', models.CharField(choices=[('N', 'Normal'), ('B', 'Benign'), ('PM', 'Pre-malignant'), ('M', 'Malignant'), ('NNP', 'Non-neoplastic Disease'), ('U', 'Undetermined'), ('HP', 'Hyperplasia'), ('MP', 'Metaplasia'), ('DP', 'Dysplasia')], max_length=50, null=True, verbose_name='Tissue type')),
                ('cell_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cell type')),
                ('pathology_disease_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pathology/disease name (for diseased samples only)')),
                ('additional_pathology_info', models.CharField(blank=True, max_length=50, null=True, verbose_name='Additional pathology information')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grade')),
                ('stage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Stage')),
                ('tumour_content', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tumor content (%)')),
                ('pathology_occurrence', models.CharField(blank=True, choices=[('PR', 'Primary'), ('RC', 'Recurrent or Relapse'), ('ME', 'Metastatic'), ('RM', 'Remission'), ('UN', 'Undetermined'), ('US', 'Unspecified')], max_length=50, null=True, verbose_name='Pathology occurrence')),
                ('treatment_status', models.CharField(blank=True, choices=[('PR', 'Pre-treatment'), ('IN', 'In-treatment'), ('PO', 'Post-treatment'), ('NA', 'N/A'), ('UN', 'Unknown')], max_length=50, null=True, verbose_name='Treatment status')),
                ('family_information', models.CharField(blank=True, max_length=50, null=True, verbose_name='Family information')),
            ],
            bases=(models.Model, core.helpers.FieldValue),
        ),
        migrations.CreateModel(
            name='ChipRegion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='region_code')),
            ],
            bases=(models.Model, core.helpers.FieldValue),
        ),
        migrations.CreateModel(
            name='ChipRegionMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metadata_value', models.CharField(blank=True, max_length=50, null=True, verbose_name='Metadata value')),
            ],
            bases=(models.Model, core.helpers.FieldValue),
        ),
        migrations.CreateModel(
            name='HistoricalAdditionalSampleInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('tissue_state', models.CharField(blank=True, choices=[('NONE', 'None'), ('FROZ', 'Frozen'), ('FRES', 'Fresh'), ('DIG-FRES', 'Digested-Fresh')], default='NONE', max_length=50, null=True, verbose_name='Tissue State')),
                ('cancer_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cancer Type')),
                ('cancer_subtype', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cancer Subtype')),
                ('disease_condition_health_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Disease condition/health status')),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('X', 'Mixed'), ('U', 'Unknown')], max_length=50, null=True, verbose_name='Sex')),
                ('patient_biopsy_date', models.DateField(blank=True, null=True, verbose_name='Patient biopsy date')),
                ('anatomic_site', models.CharField(max_length=50, null=True, verbose_name='Anatomic site')),
                ('anatomic_sub_site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Anatomic sub-site')),
                ('developmental_stage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Developmental stage')),
                ('tissue_type', models.CharField(choices=[('N', 'Normal'), ('B', 'Benign'), ('PM', 'Pre-malignant'), ('M', 'Malignant'), ('NNP', 'Non-neoplastic Disease'), ('U', 'Undetermined'), ('HP', 'Hyperplasia'), ('MP', 'Metaplasia'), ('DP', 'Dysplasia')], max_length=50, null=True, verbose_name='Tissue type')),
                ('cell_type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cell type')),
                ('pathology_disease_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pathology/disease name (for diseased samples only)')),
                ('additional_pathology_info', models.CharField(blank=True, max_length=50, null=True, verbose_name='Additional pathology information')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grade')),
                ('stage', models.CharField(blank=True, max_length=50, null=True, verbose_name='Stage')),
                ('tumour_content', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tumor content (%)')),
                ('pathology_occurrence', models.CharField(blank=True, choices=[('PR', 'Primary'), ('RC', 'Recurrent or Relapse'), ('ME', 'Metastatic'), ('RM', 'Remission'), ('UN', 'Undetermined'), ('US', 'Unspecified')], max_length=50, null=True, verbose_name='Pathology occurrence')),
                ('treatment_status', models.CharField(blank=True, choices=[('PR', 'Pre-treatment'), ('IN', 'In-treatment'), ('PO', 'Post-treatment'), ('NA', 'N/A'), ('UN', 'Unknown')], max_length=50, null=True, verbose_name='Treatment status')),
                ('family_information', models.CharField(blank=True, max_length=50, null=True, verbose_name='Family information')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical additional sample information',
                'db_table': 'additional_sample_information_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChipRegion',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('region_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='region_code')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical chip region',
                'db_table': 'chip_region_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalChipRegionMetadata',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('metadata_value', models.CharField(blank=True, max_length=50, null=True, verbose_name='Metadata value')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical chip region metadata',
                'db_table': 'chip_region_metadata_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalJiraUser',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('associated_with_dlp', models.BooleanField(default=True)),
                ('associated_with_tenx', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical jira user',
                'db_table': 'jira_user_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMetadataField',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('field', models.CharField(max_length=50, verbose_name='Metadata key')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical metadata field',
                'db_table': 'metadata_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSample',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sample_id', models.CharField(max_length=50, null=True, verbose_name='Sample ID')),
                ('taxonomy_id', models.CharField(blank=True, default='9606', max_length=50, null=True, verbose_name='Taxonomy ID')),
                ('sample_type', models.CharField(blank=True, choices=[('P', 'Patient'), ('C', 'Cell Line'), ('X', 'Xenograft'), ('Or', 'Organoid'), ('O', 'Other')], max_length=50, null=True, verbose_name='Sample type')),
                ('anonymous_patient_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Anonymous patient ID')),
                ('cell_line_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cell line ID')),
                ('xenograft_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Xenograft ID')),
                ('xenograft_recipient_taxonomy_id', models.CharField(blank=True, default='10090', max_length=50, null=True, verbose_name='Xenograft recipient taxonomy ID')),
                ('xenograft_treatment_status', models.CharField(blank=True, default='', max_length=50, verbose_name='Xenograft treatment status')),
                ('strain', models.CharField(blank=True, max_length=50, null=True, verbose_name='Strain')),
                ('xenograft_biopsy_date', models.DateField(blank=True, null=True, verbose_name='Xenograft biopsy date')),
                ('notes', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Notes')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical sample',
                'db_table': 'history_sample',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSublibraryInformation',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('sample', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sample')),
                ('row', models.IntegerField(blank=True, null=True, verbose_name='Row')),
                ('column', models.IntegerField(blank=True, null=True, verbose_name='Column')),
                ('img_col', models.IntegerField(blank=True, null=True, verbose_name='Image Column')),
                ('file_ch1', models.CharField(blank=True, max_length=50, null=True, verbose_name='File_Ch1')),
                ('file_ch2', models.CharField(blank=True, max_length=50, null=True, verbose_name='File_Ch2')),
                ('fld_section', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fld_Section')),
                ('fld_index', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fld_Index')),
                ('num_live', models.IntegerField(blank=True, null=True, verbose_name='Num_Live')),
                ('num_dead', models.IntegerField(blank=True, null=True, verbose_name='Num_Dead')),
                ('num_other', models.IntegerField(blank=True, null=True, verbose_name='Num_Other')),
                ('rev_live', models.IntegerField(blank=True, null=True, verbose_name='Rev_Live')),
                ('rev_dead', models.IntegerField(blank=True, null=True, verbose_name='Rev_Dead')),
                ('rev_other', models.IntegerField(blank=True, null=True, verbose_name='Rev_Other')),
                ('condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='experimental_condition')),
                ('index_i7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Index_I7')),
                ('primer_i7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer_I7')),
                ('index_i5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Index_I5')),
                ('primer_i5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer_I5')),
                ('pick_met', models.CharField(blank=True, max_length=50, null=True, verbose_name='cell_call')),
                ('spot_well', models.CharField(blank=True, max_length=50, null=True, verbose_name='Spot_Well')),
                ('num_drops', models.IntegerField(blank=True, null=True, verbose_name='Num_Drops')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical sublibrary information',
                'db_table': 'sub_library_information_history',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='JiraUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('associated_with_dlp', models.BooleanField(default=True)),
                ('associated_with_tenx', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetadataField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(max_length=50, verbose_name='Metadata key')),
            ],
        ),
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
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample_id', models.CharField(max_length=50, null=True, verbose_name='Sample ID')),
                ('taxonomy_id', models.CharField(blank=True, default='9606', max_length=50, null=True, verbose_name='Taxonomy ID')),
                ('sample_type', models.CharField(blank=True, choices=[('P', 'Patient'), ('C', 'Cell Line'), ('X', 'Xenograft'), ('Or', 'Organoid'), ('O', 'Other')], max_length=50, null=True, verbose_name='Sample type')),
                ('anonymous_patient_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Anonymous patient ID')),
                ('cell_line_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Cell line ID')),
                ('xenograft_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Xenograft ID')),
                ('xenograft_recipient_taxonomy_id', models.CharField(blank=True, default='10090', max_length=50, null=True, verbose_name='Xenograft recipient taxonomy ID')),
                ('xenograft_treatment_status', models.CharField(blank=True, default='', max_length=50, verbose_name='Xenograft treatment status')),
                ('strain', models.CharField(blank=True, max_length=50, null=True, verbose_name='Strain')),
                ('xenograft_biopsy_date', models.DateField(blank=True, null=True, verbose_name='Xenograft biopsy date')),
                ('notes', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Notes')),
            ],
            options={
                'ordering': ['sample_id'],
            },
            bases=(models.Model, core.helpers.FieldValue),
        ),
        migrations.CreateModel(
            name='SublibraryInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sample')),
                ('row', models.IntegerField(blank=True, null=True, verbose_name='Row')),
                ('column', models.IntegerField(blank=True, null=True, verbose_name='Column')),
                ('img_col', models.IntegerField(blank=True, null=True, verbose_name='Image Column')),
                ('file_ch1', models.CharField(blank=True, max_length=50, null=True, verbose_name='File_Ch1')),
                ('file_ch2', models.CharField(blank=True, max_length=50, null=True, verbose_name='File_Ch2')),
                ('fld_section', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fld_Section')),
                ('fld_index', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fld_Index')),
                ('num_live', models.IntegerField(blank=True, null=True, verbose_name='Num_Live')),
                ('num_dead', models.IntegerField(blank=True, null=True, verbose_name='Num_Dead')),
                ('num_other', models.IntegerField(blank=True, null=True, verbose_name='Num_Other')),
                ('rev_live', models.IntegerField(blank=True, null=True, verbose_name='Rev_Live')),
                ('rev_dead', models.IntegerField(blank=True, null=True, verbose_name='Rev_Dead')),
                ('rev_other', models.IntegerField(blank=True, null=True, verbose_name='Rev_Other')),
                ('condition', models.CharField(blank=True, max_length=50, null=True, verbose_name='experimental_condition')),
                ('index_i7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Index_I7')),
                ('primer_i7', models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer_I7')),
                ('index_i5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Index_I5')),
                ('primer_i5', models.CharField(blank=True, max_length=50, null=True, verbose_name='Primer_I5')),
                ('pick_met', models.CharField(blank=True, max_length=50, null=True, verbose_name='cell_call')),
                ('spot_well', models.CharField(blank=True, max_length=50, null=True, verbose_name='Spot_Well')),
                ('num_drops', models.IntegerField(blank=True, null=True, verbose_name='Num_Drops')),
                ('chip_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ChipRegion', verbose_name='Chip_Region')),
            ],
            bases=(models.Model, core.helpers.FieldValue),
        ),
    ]
