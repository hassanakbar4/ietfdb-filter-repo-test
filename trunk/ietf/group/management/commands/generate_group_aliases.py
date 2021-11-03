# Copyright The IETF Trust 2012-2021, All Rights Reserved
# -*- coding: utf-8 -*-

# This was written as a script by Markus Stenberg <markus.stenberg@iki.fi>.
# It was turned into a management command by Russ Housley <housley@vigisec.com>.

import datetime
import io
import os
import time
    
from django.conf import settings
from django.core.management.base import BaseCommand

import debug                            # pyflakes:ignore

from ietf.group.models import Group
from ietf.group.utils import get_group_ad_emails, get_group_role_emails, get_child_group_role_emails
from ietf.name.models import GroupTypeName
from ietf.utils.aliases import dump_sublist

DEFAULT_YEARS = 5
ACTIVE_STATES=['active','bof','proposed']
GROUP_TYPES=['wg','rg','dir','team','review','program']
NO_AD_GROUP_TYPES=['rg','team','program']
IETF_DOMAIN=['ietf.org', ]
IRTF_DOMAIN=['irtf.org', ]
IAB_DOMAIN=['iab.org', ]

class Command(BaseCommand):
    help = ('Generate the group-aliases and group-virtual files for Internet-Draft '
            'mail aliases, placing them in the file configured in '
            'settings.GROUP_ALIASES_PATH and settings.GROUP_VIRTUAL_PATH, '
            'respectively.  The generation includes aliases for groups that '
            'have seen activity in the last %s years.' % (DEFAULT_YEARS))

    def handle(self, *args, **options):
        show_since = datetime.datetime.now() - datetime.timedelta(DEFAULT_YEARS*365)

        date = time.strftime("%Y-%m-%d_%H:%M:%S")
        signature = '# Generated by %s at %s\n' % (os.path.abspath(__file__), date)

        afile = io.open(settings.GROUP_ALIASES_PATH, "w")
        vfile = io.open(settings.GROUP_VIRTUAL_PATH, "w")

        afile.write(signature)
        vfile.write(signature)
        vfile.write("%s anything\n" % settings.GROUP_VIRTUAL_DOMAIN)

        # Loop through each group type and build -ads and -chairs entries
        for g in GROUP_TYPES:
            domains = []
            domains += IETF_DOMAIN
            if g == 'rg':
                domains += IRTF_DOMAIN
            if g == 'program':
                domains += IAB_DOMAIN

            entries = Group.objects.filter(type=g).all()
            active_entries = entries.filter(state__in=ACTIVE_STATES)
            inactive_recent_entries = entries.exclude(state__in=ACTIVE_STATES).filter(time__gte=show_since)
            interesting_entries = active_entries | inactive_recent_entries

            for e in interesting_entries.distinct().iterator():
                name = e.acronym
                
                # Research groups, teams, and programs do not have -ads lists
                if not g in NO_AD_GROUP_TYPES:
                    dump_sublist(afile, vfile, name+'-ads', domains, settings.GROUP_VIRTUAL_DOMAIN, get_group_ad_emails(e))
                # All group types have -chairs lists
                dump_sublist(afile, vfile, name+'-chairs', domains, settings.GROUP_VIRTUAL_DOMAIN, get_group_role_emails(e, ['chair', 'secr']))

        # The area lists include every chair in active working groups in the area
        areas = Group.objects.filter(type='area').all()
        active_areas = areas.filter(state__in=ACTIVE_STATES)
        for area in active_areas:
            name = area.acronym
            area_ad_emails = get_group_role_emails(area, ['pre-ad', 'ad', 'chair'])
            dump_sublist(afile, vfile, name+'-ads', IETF_DOMAIN, settings.GROUP_VIRTUAL_DOMAIN, area_ad_emails)
            dump_sublist(afile, vfile, name+'-chairs', IETF_DOMAIN, settings.GROUP_VIRTUAL_DOMAIN, (get_child_group_role_emails(area, ['chair', 'secr']) | area_ad_emails))

        # Other groups with chairs that require Internet-Draft submission approval
        gtypes = GroupTypeName.objects.values_list('slug', flat=True)
        special_groups = Group.objects.filter(type__features__req_subm_approval=True, acronym__in=gtypes, state='active')
        for group in special_groups:
            dump_sublist(afile, vfile, group.acronym+'-chairs', IETF_DOMAIN, settings.GROUP_VIRTUAL_DOMAIN, get_group_role_emails(group, ['chair', 'delegate']))

        afile.close()
        vfile.close()