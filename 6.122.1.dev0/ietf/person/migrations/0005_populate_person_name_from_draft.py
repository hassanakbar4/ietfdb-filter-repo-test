# Copyright The IETF Trust 2018-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-10 05:28


from __future__ import absolute_import, print_function, unicode_literals

import sys

from django.db import migrations

import debug                            # pyflakes:ignore

def populate_person_name_from_draft(apps, schema_editor):
    Submission      = apps.get_model('submit', 'Submission')
    Email           = apps.get_model('person', 'Email')
    #
    sys.stdout.write("\n")
    #
    sys.stdout.write("\n    ** This migration may take some time.  Expect at least a few minutes **.\n\n")
    sys.stdout.write("    Initializing data structures...\n")
    persons = dict([ (e.address, e.person) for e in Email.objects.all() ])

    count = 0
    sys.stdout.write("    Assigning Person.name_from_draft from Submission records...\n")
    for o in Submission.objects.all().order_by('-submission_date'):
        for a in o.authors:
            name  = a['name']
            email = a['email']
            if email in persons:
                p = persons[email]
                if not p.name_from_draft:
                    p.name_from_draft = name
                    count += 1
                    p.save()
                del persons[email]
    sys.stdout.write("    Submission author names assigned: %d\n" % count)

def reverse(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_populate_email_origin'),
    ]

    operations = [
        migrations.RunPython(populate_person_name_from_draft, reverse)
    ]
