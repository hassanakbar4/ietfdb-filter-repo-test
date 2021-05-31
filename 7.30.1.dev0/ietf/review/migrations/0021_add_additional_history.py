# Copyright The IETF Trust 2019-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-19 04:36


import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ietf.utils.models
import ietf.utils.validators
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_auto_20190118_0725'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doc', '0026_add_draft_rfceditor_state'),
        ('name', '0007_fix_m2m_slug_id_length'),
        ('group', '0019_rename_field_document2'),
        ('review', '0020_auto_20191115_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalReviewAssignment',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_change_reason', models.TextField(null=True)),
                ('assigned_on', models.DateTimeField(blank=True, null=True)),
                ('completed_on', models.DateTimeField(blank=True, null=True)),
                ('reviewed_rev', models.CharField(blank=True, max_length=16, verbose_name='reviewed revision')),
                ('mailarch_url', models.URLField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('result', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='name.ReviewResultName')),
                ('review', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='doc.Document')),
            ],
            options={
                'verbose_name': 'historical review assignment',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReviewRequest',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_change_reason', models.TextField(null=True)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('deadline', models.DateField()),
                ('requested_rev', models.CharField(blank=True, help_text='Fill in if a specific revision is to be reviewed, e.g. 02', max_length=16, verbose_name='requested revision')),
                ('comment', models.TextField(blank=True, default='', help_text='Provide any additional information to show to the review team secretary and reviewer', max_length=2048, verbose_name="Requester's comments and instructions")),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('doc', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='doc.Document')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('requested_by', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='person.Person')),
                ('state', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='name.ReviewRequestStateName')),
                ('team', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group')),
                ('type', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='name.ReviewTypeName')),
            ],
            options={
                'verbose_name': 'historical review request',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalUnavailablePeriod',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('history_change_reason', models.TextField(null=True)),
                ('start_date', models.DateField(default=datetime.date.today, help_text="Choose the start date so that you can still do a review if it's assigned just before the start date - this usually means you should mark yourself unavailable for assignment some time before you are actually away. The default is today.", null=True)),
                ('end_date', models.DateField(blank=True, help_text='Leaving the end date blank means that the period continues indefinitely. You can end it later.', null=True)),
                ('availability', models.CharField(choices=[('canfinish', 'Can do follow-ups'), ('unavailable', 'Completely unavailable')], max_length=30)),
                ('reason', models.TextField(blank=True, default='', help_text="Provide (for the secretary's benefit) the reason why the review is unavailable", max_length=2048, verbose_name='Reason why reviewer is unavailable (Optional)')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('person', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='person.Person')),
                ('team', ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='group.Group')),
            ],
            options={
                'verbose_name': 'historical unavailable period',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='expertise',
            field=models.TextField(blank=True, default='', help_text="Describe the reviewer's expertise in this team's area", max_length=2048, verbose_name="Reviewer's expertise in this team's area"),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='filter_re',
            field=models.CharField(blank=True, help_text='Draft names matching this regular expression should not be assigned', max_length=255, validators=[ietf.utils.validators.RegexStringValidator()], verbose_name='Filter regexp'),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='min_interval',
            field=models.IntegerField(blank=True, choices=[(7, 'Once per week'), (14, 'Once per fortnight'), (30, 'Once per month'), (61, 'Once per two months'), (91, 'Once per quarter')], null=True, verbose_name='Can review at most'),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='remind_days_before_deadline',
            field=models.IntegerField(blank=True, help_text="To get an email reminder in case you forget to do an assigned review, enter the number of days before review deadline you want to receive it. Clear the field if you don't want this reminder.", null=True),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='remind_days_open_reviews',
            field=models.PositiveIntegerField(blank=True, help_text="To get a periodic email reminder of all your open reviews, enter the number of days between these reminders. Clear the field if you don't want these reminders.", null=True, verbose_name='Periodic reminder of open reviews every X days'),
        ),
        migrations.AlterField(
            model_name='historicalreviewersettings',
            name='skip_next',
            field=models.IntegerField(default=0, verbose_name='Skip next assignments'),
        ),
        migrations.AlterField(
            model_name='reviewassignment',
            name='reviewed_rev',
            field=models.CharField(blank=True, max_length=16, verbose_name='reviewed revision'),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='expertise',
            field=models.TextField(blank=True, default='', help_text="Describe the reviewer's expertise in this team's area", max_length=2048, verbose_name="Reviewer's expertise in this team's area"),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='filter_re',
            field=models.CharField(blank=True, help_text='Draft names matching this regular expression should not be assigned', max_length=255, validators=[ietf.utils.validators.RegexStringValidator()], verbose_name='Filter regexp'),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='min_interval',
            field=models.IntegerField(blank=True, choices=[(7, 'Once per week'), (14, 'Once per fortnight'), (30, 'Once per month'), (61, 'Once per two months'), (91, 'Once per quarter')], null=True, verbose_name='Can review at most'),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='remind_days_before_deadline',
            field=models.IntegerField(blank=True, help_text="To get an email reminder in case you forget to do an assigned review, enter the number of days before review deadline you want to receive it. Clear the field if you don't want this reminder.", null=True),
        ),
        migrations.AlterField(
            model_name='reviewersettings',
            name='skip_next',
            field=models.IntegerField(default=0, verbose_name='Skip next assignments'),
        ),
        migrations.AlterField(
            model_name='reviewrequest',
            name='comment',
            field=models.TextField(blank=True, default='', help_text='Provide any additional information to show to the review team secretary and reviewer', max_length=2048, verbose_name="Requester's comments and instructions"),
        ),
        migrations.AlterField(
            model_name='reviewrequest',
            name='requested_rev',
            field=models.CharField(blank=True, help_text='Fill in if a specific revision is to be reviewed, e.g. 02', max_length=16, verbose_name='requested revision'),
        ),
        migrations.AlterField(
            model_name='reviewsecretarysettings',
            name='remind_days_before_deadline',
            field=models.IntegerField(blank=True, help_text="To get an email reminder in case a reviewer forgets to do an assigned review, enter the number of days before review deadline you want to receive it. Clear the field if you don't want a reminder.", null=True),
        ),
        migrations.AlterField(
            model_name='reviewteamsettings',
            name='autosuggest',
            field=models.BooleanField(default=True, verbose_name='Automatically suggest possible review requests'),
        ),
        migrations.AlterField(
            model_name='reviewteamsettings',
            name='remind_days_unconfirmed_assignments',
            field=models.PositiveIntegerField(blank=True, help_text="To send a periodic email reminder to reviewers of review assignments they have neither accepted nor rejected, enter the number of days between these reminders. Clear the field if you don't want these reminders to be sent.", null=True, verbose_name='Periodic reminder of not yet accepted or rejected review assignments to reviewer every X days'),
        ),
        migrations.AlterField(
            model_name='reviewteamsettings',
            name='secr_mail_alias',
            field=models.CharField(blank=True, help_text='Email alias for all of the review team secretaries', max_length=255, verbose_name='Email alias for all of the review team secretaries'),
        ),
        migrations.AlterField(
            model_name='unavailableperiod',
            name='availability',
            field=models.CharField(choices=[('canfinish', 'Can do follow-ups'), ('unavailable', 'Completely unavailable')], max_length=30),
        ),
        migrations.AlterField(
            model_name='unavailableperiod',
            name='end_date',
            field=models.DateField(blank=True, help_text='Leaving the end date blank means that the period continues indefinitely. You can end it later.', null=True),
        ),
        migrations.AlterField(
            model_name='unavailableperiod',
            name='reason',
            field=models.TextField(blank=True, default='', help_text="Provide (for the secretary's benefit) the reason why the review is unavailable", max_length=2048, verbose_name='Reason why reviewer is unavailable (Optional)'),
        ),
        migrations.AlterField(
            model_name='unavailableperiod',
            name='start_date',
            field=models.DateField(default=datetime.date.today, help_text="Choose the start date so that you can still do a review if it's assigned just before the start date - this usually means you should mark yourself unavailable for assignment some time before you are actually away. The default is today.", null=True),
        ),
        migrations.AddField(
            model_name='historicalreviewassignment',
            name='review_request',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='review.ReviewRequest'),
        ),
        migrations.AddField(
            model_name='historicalreviewassignment',
            name='reviewer',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='person.Email'),
        ),
        migrations.AddField(
            model_name='historicalreviewassignment',
            name='state',
            field=ietf.utils.models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='name.ReviewAssignmentStateName'),
        ),
    ]
