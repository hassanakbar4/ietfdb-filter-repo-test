# Copyright The IETF Trust 2015-2020, All Rights Reserved
# -*- coding: utf-8 -*-


from __future__ import absolute_import, print_function, unicode_literals


import collections
import datetime

import django
django.setup()

from django.core.management.base import BaseCommand #, CommandError

import debug                            # pyflakes:ignore

from ietf.doc.models import NewRevisionDocEvent
from ietf.submit.models import Submission, SubmissionEvent

RevInfo = collections.namedtuple('RevInfo', ['doc', 'event', 'rev'])

class Command(BaseCommand):
    help = """
    Check that new revision events for drafts have monotonically increasing
    revision numbers and that the latest event revision number matches the
    document revision number.
    """

    def add_arguments(self, parser):
        default_start = datetime.datetime.now() - datetime.timedelta(days=60)
        parser.add_argument(
            '-d', '--from', type=str, default=default_start.strftime('%Y-%m-%d'),
            help='Limit the list to messages saved after the given date (default %(default)s).',
        )
        parser.add_argument('documents', nargs='*',
            help="One or more files to process")

    def check_objects(self, queryset, timeattr, docattr):
        revs = {}
        self.stdout.write("  Checking %s ..." % queryset.model.__name__)
        for obj in queryset:
            doc =  getattr(obj, docattr)
            time = getattr(obj, timeattr)
            if not obj.rev:
                self.stdout.write("Bad revision number: %s %-52s: '%s'" % (time, doc.name, obj.rev))
                continue
            rev = int(obj.rev.lstrip('0') or '0')
            #self.stdout.write("%s %-52s %02s" % (time, doc.name, obj.rev))
            if doc.name in revs:
                if rev <= revs[doc.name].rev:
                    self.stderr.write("%s %-50s %02d -> %02d" % (time, doc.name, revs[doc.name].rev, rev))
            revs[doc.name] = RevInfo(doc, obj, rev)
        for doc, obj, rev in revs.values():
            if not doc.rev == obj.rev:
                self.stderr.write("%-50s: doc.rev: %s != %s.rev: %s" % (doc.name, doc.rev, obj._meta.model_name, obj.rev))


    def handle(self, *args, **options):
        #verbosity = options.get("verbosity", 1)

        self.stdout.write("Checking submissions from %s" % options['from'])

        for model, timeattr, docattr in [
                (NewRevisionDocEvent, 'time', 'doc'),
                (Submission, 'submission_date', 'draft'),
            ]:
            filter = {
                '%s__gte'%timeattr:     options['from'],
                '%s__type_id' %docattr: 'draft',           
                }
            qs = model.objects.filter(**filter).order_by(timeattr)
            if options['documents']:
                docfilter = {
                    '%s__name__in' % docattr: options['documents'],
                    }
                qs = qs.filter(**docfilter)

            self.check_objects(qs, timeattr, docattr)
