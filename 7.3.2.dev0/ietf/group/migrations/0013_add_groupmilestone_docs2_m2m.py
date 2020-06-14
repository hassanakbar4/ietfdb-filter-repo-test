# Copyright The IETF Trust 2019-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-25 13:02


from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models

class Migration(migrations.Migration):

    dependencies = [
        ('group', '0012_add_old_nomcom_announcements'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMilestoneDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document', to_field=b'id')),
                ('groupmilestone', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.GroupMilestone')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMilestoneHistoryDocs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doc.Document', to_field=b'id')),
                ('groupmilestonehistory', ietf.utils.models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.GroupMilestoneHistory')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='charter2',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chartered_group', to='doc.Document', to_field='id'),
        ),
        migrations.AlterField(
            model_name='group',
            name='charter',
            field=ietf.utils.models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='old_group', to='doc.Document', to_field='name'),
        ),
        migrations.AddField(
            model_name='groupmilestone',
            name='docs2',
            field=models.ManyToManyField(blank=True, related_name='groupmilestones', through='group.GroupMilestoneDocs', to='doc.Document'),
        ),
        migrations.AddField(
            model_name='groupmilestonehistory',
            name='docs2',
            field=models.ManyToManyField(blank=True, related_name='groupmilestoneshistory', through='group.GroupMilestoneHistoryDocs', to='doc.Document'),
        ),
    ]
