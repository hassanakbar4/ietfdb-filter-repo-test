# Copyright The IETF Trust 2018-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-23 15:11


from __future__ import absolute_import, print_function, unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unavailableperiod',
            name='reason',
            field=models.TextField(blank=True, default=b'', help_text=b"Provide (for the secretary's benefit) the reason why the review is unavailable", max_length=2048, verbose_name=b'Reason why reviewer is unavailable (Optional)'),
        ),
    ]
