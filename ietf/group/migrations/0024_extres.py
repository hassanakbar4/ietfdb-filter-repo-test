# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-15 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('name', '0011_populate_extres'),
        ('group', '0023_use_milestone_dates_default_to_true'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupExtResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display_name', models.CharField(blank=True, default='', max_length=255)),
                ('value', models.CharField(max_length=2083)),
                ('group', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='name.ExtResourceName')),
            ],
        ),
    ]
