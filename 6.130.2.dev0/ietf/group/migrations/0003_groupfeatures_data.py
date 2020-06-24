# Copyright The IETF Trust 2018-2020, All Rights Reserved
# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-10 15:58


from django.conf import settings
from django.db import migrations

import debug                            # pyflakes:ignore

from ietf.review.utils import active_review_teams

group_type_features = {
    'ag': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': True,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'area': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'dir': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair,secr',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'review': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair,secr',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.review_requests',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': True,
        'material_types': 'slides'},
    'iab': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': True,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'ietf': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': True,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'individ': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'irtf': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'isoc': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'nomcom': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'side',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'program': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'lead',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': True,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': True,
        'has_reviews': False,
        'material_types': 'slides'},
    'rfcedtyp': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'side',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'rg': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': True,
        'default_tab': 'ietf.group.views.group_documents',
        'has_chartering_process': True,
        'has_default_jabber': True,
        'has_dependencies': True,
        'has_documents': True,
        'has_meetings': True,
        'has_nonsession_materials': False,
        'has_milestones': True,
        'has_reviews': False,
        'material_types': 'slides'},
    'sdo': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': None,
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': False,
        'has_nonsession_materials': False,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'team': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': False,
        'default_tab': 'ietf.group.views.group_about',
        'has_chartering_process': False,
        'has_default_jabber': False,
        'has_dependencies': False,
        'has_documents': False,
        'has_meetings': True,
        'has_nonsession_materials': True,
        'has_milestones': False,
        'has_reviews': False,
        'material_types': 'slides'},
    'wg': {
        'about_page': 'ietf.group.views.group_about',
        'admin_roles': 'chair',
        'agenda_type': 'ietf',
        'customize_workflow': True,
        'default_tab': 'ietf.group.views.group_documents',
        'has_chartering_process': True,
        'has_default_jabber': True,
        'has_dependencies': True,
        'has_documents': True,
        'has_meetings': True,
        'has_nonsession_materials': False,
        'has_milestones': True,
        'has_reviews': False,
        'material_types': 'slides'},
}


def forward(apps, schema_editor):
    Group = apps.get_model('group', 'Group')
    GroupTypeName = apps.get_model('name', 'GroupTypeName')
    GroupFeatures = apps.get_model('group', 'GroupFeatures')
    AgendaTypeName = apps.get_model('name', 'AgendaTypeName')
    for type in group_type_features:
        features = group_type_features[type]
        features['type_id'] = type
        if features['agenda_type']:
            features['agenda_type'] = AgendaTypeName.objects.get(slug=features['agenda_type'])
        GroupFeatures.objects.create(**features)
    dir = GroupTypeName.objects.get(slug='dir')
    review = GroupTypeName.objects.create(slug='review', name='Directorate (with reviews)', desc='', used=True, order=0)
    review_teams = [ g.acronym for g in active_review_teams() ]
    for group in Group.objects.filter(type=dir):
        if group.acronym in review_teams:
            group.type = review
            group.save()

def reverse(apps, schema_editor):
    Group = apps.get_model('group', 'Group')
    GroupFeatures = apps.get_model('group', 'GroupFeatures')
    GroupTypeName = apps.get_model('name', 'GroupTypeName')
    dir = GroupTypeName.objects.get(slug='dir')
    review = GroupTypeName.objects.get(slug='review')
    for group in Group.objects.filter(type=review):
        group.type = dir
        group.save()
    for entry in GroupFeatures.objects.all():
        entry.delete()
    review.delete()

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0002_groupfeatures_historicalgroupfeatures'),
        ('name', '0003_agendatypename_data'),
    ]

    operations = [
        migrations.RunPython(forward, reverse),
    ]
