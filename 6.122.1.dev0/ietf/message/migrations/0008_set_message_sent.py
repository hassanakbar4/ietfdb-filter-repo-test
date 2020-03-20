# Copyright The IETF Trust 2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-21 14:27


from __future__ import absolute_import, print_function, unicode_literals

from tqdm import tqdm

from django.db import migrations


def forward(apps, schema_editor):

    Message                     = apps.get_model('message', 'Message')

    for m in tqdm(Message.objects.filter(sent=None)):
        if m.sendqueue_set.exists():
            q = m.sendqueue_set.last()
            m.sent = q.sent_at
        else:
            m.sent = m.time
        m.save()

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_message_sent'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
