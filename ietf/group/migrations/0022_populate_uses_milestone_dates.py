# Copyright The IETF Trust 2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-30 11:42
from __future__ import unicode_literals

from django.db import migrations

def forward(apps, schema_editor):
    Group = apps.get_model('group','Group')
    GroupHistory = apps.get_model('group','GroupHistory')

    Group.objects.filter(type__features__has_milestones=True).update(uses_milestone_dates=True)
    GroupHistory.objects.filter(type__features__has_milestones=True).update(uses_milestone_dates=True)

def reverse(apps, schema_editor):
    Group = apps.get_model('group','Group')
    GroupHistory = apps.get_model('group','GroupHistory')

    Group.objects.filter(type__features__has_milestones=True).update(uses_milestone_dates=False)
    GroupHistory.objects.filter(type__features__has_milestones=True).update(uses_milestone_dates=False)

class Migration(migrations.Migration):

    dependencies = [
        ('group', '0021_add_order_to_milestones'),
    ]

    operations = [
        migrations.RunPython(forward, reverse)
    ]
