# Copyright The IETF Trust 2019-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-10 04:36


import sys

from tqdm import tqdm

from django.db import migrations, models


def forward(apps, schema_editor):
    DocAlias = apps.get_model('doc','DocAlias')
    sys.stderr.write('\n')
    for a in tqdm(DocAlias.objects.all()):
        a.docs.add(a.document)

def reverse(apps, schema_editor):
    DocAlias = apps.get_model('doc','DocAlias')
    sys.stderr.write('\n')
    for a in tqdm(DocAlias.objects.all()):
        a.document = a.document
        a.save()

class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0022_document_primary_key_cleanup'),
    ]

    operations = [
        migrations.AddField(
            model_name='docalias',
            name='docs',
            field=models.ManyToManyField(related_name='docalias', to='doc.Document'),
        ),
        migrations.RunPython(forward, reverse),
        migrations.RemoveField(
            model_name='docalias',
            name='document',
        ),
    ]