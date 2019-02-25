# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-02-25 19:54
from __future__ import unicode_literals
from datetime import date
from django.db import migrations
from core.models import DlpLibrary as DlpLibraryModel

library_ids = [
    'A90679',
    'A96165A',
    'A96179B',
    'A96186C',
    'A95732B',
    'A96174B',
    'A96130B',
    'A96177B',
    'A96145A',
    'A96219B',
    'A96172A',
    'A95724A',
    'A95662B',
    'A95664B',
    'A95621D',
    'A95635D',
    'A95662A',
    'A95724B',
    'A95632B',
    'A95632C',
    'A95632D',
    'A95635B',
    'A95635C',
    'A96225A',
    'A95728A',
    'A96130A',
    'A96184A',
    'A96217B',
    'A90565',
    'A90690',
    'A96174A',
    'A96187A',
    'A96173A',
    'A95621B',
    'A96109A',
    'A96171A',
    'MF1509041',
    'MF1509042',
    'MF1508181',
    'MF1508182',
    'A90703ABC',
    'A90704ABC',
    'A95670A',
    'A95670B',
    'A90696ABC',
    'A90696B',
    'A90696C',
    'A90697ABC',
    'A96165B',
    'A96177A',
    'A95732A',
    'A96215B',
    'A95736A',
    'A96177C',
    'A96180A',
    'A95722A',
    'A96214B',
    'A96175A',
    'A96212B',
    'A96164A',
    'A96214A',
    'A96210A',
    'A96212A',
    'A96169B',
    'A96211B',
    'A96169A',
    'A96197C',
    'A96222B',
    'A96164B',
    'A96211A',
    'A96224C',
    'A90632',
    'A96210B',
    'A95664A',
    'A96170A',
    'A96170B',
    'A96216B',
    'A96179A',
    'A96186B',
    'A73044B',
    'A73047D',
    'A96199B',
    'A73046B',
    'A73056B',
    'A90554C',
    'A90600C',
    'A95660A',
    'A96155B',
    'A96172B',
    'A96175C',
    'A96180B',
    'A96183C',
    'A96186A',
    'A96208A',
    'A96210C',
    'A96211C',
    'A96215A',
    'A96216A',
    'A95632A',
    'A95621A',
    'A95635A',
    'A96155C',
    'A96181C',
    'A96183B',
    'A96225B',
    'A96225C',
    'A90706',
    'A90685',
    'A90553A',
    'A90689B',
    'A90689C',
    'A73044A',
    'A90553C',
    'A90648B',
    'A90694A',
    'A90694B',
    'A75617A',
    'A90682',
    'A90560A',
    'A90554A',
    'A96213A',
    'A90554B',
    'A96139A',
    'A96147A',
    'A96150A',
    'A95622A',
    'A95624A',
    'A90560B',
    'A96156A',
    'A96156B',
    'A96176A',
    'A96222A',
    'A96141A',
    'A96161B',
    'A96146B',
    'A96146A',
    'A96220B',
    'A96141B',
    'A96226A',
    'A96226B',
    'A96157C',
    'A96149B',
    'A96228B',
    'A96149A',
    'A96228A',
    'A96199A',
    'A96157B',
    'A96158A',
    'A96141B',
    'A96240B',
    'A96162A',
    'A96162B',
    'A96240A',
    'A96199A',
    'A96155A',
    'A96161A',
    'A96168B',
    'A96181B',
    'A96192A',
    'A96203A',
    'A96206A',
    'A96206B',
    'A96163A',
    'A96163B',
    'A96189A',
    'A96189B',
    'A96190A',
    'A96190B',
    'A96193A',
    'A96193B',
    'A96194A',
    'A96194B',
    'A96204A',
    'A96205A',
    'A96205B',
    'A96207B',
    'A96229B',
    'A96233A',
    'A96233B',
    'A96244A',
    'A96244B',
    'A95650B',
    'A95717A',
    'A96229A',
    'A96210B',
    'A95675B',
    'A95634B',
    'A95675A',
    'A95720A',
    'A95668B',
    'A95668A',
    'A96201B',
    'A96201A',
    'A95629B',
    'A95629A',
    'A95673A',
    'A95720B',
    'A95634A',
    'A95650A',
    'A96195A',
    'A95717B',
    'A96207A',
    'A98202A',
    'A96204B',
    'A96192B',
    'A75617B',
    'A75617BC',
    'A90545',
    'A72833',
    'A96224B',
    'A90658B',
    'A90578',
    'A72931',
    'A72932',
    'A72934',
    'A72920',
    'A90707',
    'A75616C',
]

def update_exclude_from_analysis(apps, schema_editor):
    libraries = DlpLibraryModel.objects.all()

    for library in libraries:
        if library.pool_id in library_ids:
            library.exclude_from_analysis = True
        elif (date.today() - library.history.earliest().history_date.date()).days/(365/12) > 4:
            library.exclude_from_analysis = True
        else:
            pass

        library.save()



class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_auto_20190225_1145'),
    ]

    operations = [
        migrations.RunPython(update_exclude_from_analysis)
    ]
