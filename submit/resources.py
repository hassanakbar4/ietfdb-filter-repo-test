# Copyright The IETF Trust 2014-2019, All Rights Reserved
# -*- coding: utf-8 -*-
# Autogenerated by the mkresources management command 2014-11-13 23:53


from ietf.api import ModelResource
from tastypie.fields import ToOneField, ToManyField
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.cache import SimpleCache

from ietf import api
from ietf.submit.models import ( Preapproval, SubmissionCheck, Submission,
    SubmissionEmailEvent, SubmissionEvent )
from ietf.person.resources import PersonResource


class PreapprovalResource(ModelResource):
    by               = ToOneField(PersonResource, 'by')
    class Meta:
        cache = SimpleCache()
        queryset = Preapproval.objects.all()
        serializer = api.Serializer()
        #resource_name = 'preapproval'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "name": ALL,
            "time": ALL,
            "by": ALL_WITH_RELATIONS,
        }
api.submit.register(PreapprovalResource())

from ietf.group.resources import GroupResource
from ietf.name.resources import DraftSubmissionStateNameResource
from ietf.doc.resources import DocumentResource
class SubmissionResource(ModelResource):
    state            = ToOneField(DraftSubmissionStateNameResource, 'state')
    group            = ToOneField(GroupResource, 'group', null=True)
    draft            = ToOneField(DocumentResource, 'draft', null=True)
    checks           = ToManyField('ietf.submit.resources.SubmissionCheckResource', 'checks', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = Submission.objects.all()
        serializer = api.Serializer()
        #resource_name = 'submission'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "remote_ip": ALL,
            "access_key": ALL,
            "auth_key": ALL,
            "name": ALL,
            "title": ALL,
            "abstract": ALL,
            "rev": ALL,
            "pages": ALL,
            "authors": ALL,
            "note": ALL,
            "replaces": ALL,
            "first_two_pages": ALL,
            "file_types": ALL,
            "file_size": ALL,
            "document_date": ALL,
            "submission_date": ALL,
            "submitter": ALL,
            "xml_version": ALL,
            "state": ALL_WITH_RELATIONS,
            "group": ALL_WITH_RELATIONS,
            "draft": ALL_WITH_RELATIONS,
        }
api.submit.register(SubmissionResource())

from ietf.person.resources import PersonResource
class SubmissionEventResource(ModelResource):
    submission       = ToOneField(SubmissionResource, 'submission')
    by               = ToOneField(PersonResource, 'by', null=True)
    class Meta:
        cache = SimpleCache()
        queryset = SubmissionEvent.objects.all()
        serializer = api.Serializer()
        #resource_name = 'submissionevent'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "desc": ALL,
            "submission": ALL_WITH_RELATIONS,
            "by": ALL_WITH_RELATIONS,
        }
api.submit.register(SubmissionEventResource())

class SubmissionCheckResource(ModelResource):
    submission       = ToOneField(SubmissionResource, 'submission')
    class Meta:
        cache = SimpleCache()
        queryset = SubmissionCheck.objects.all()
        serializer = api.Serializer()
        #resource_name = 'submissioncheck'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "checker": ALL,
            "passed": ALL,
            "message": ALL,
            "errors": ALL,
            "warnings": ALL,
            "items": ALL,
            "submission": ALL_WITH_RELATIONS,
        }
api.submit.register(SubmissionCheckResource())



from ietf.person.resources import PersonResource
from ietf.message.resources import MessageResource
class SubmissionEmailEventResource(ModelResource):
    submission       = ToOneField(SubmissionResource, 'submission')
    by               = ToOneField(PersonResource, 'by', null=True)
    submissionevent_ptr = ToOneField(SubmissionEventResource, 'submissionevent_ptr')
    message          = ToOneField(MessageResource, 'message', null=True)
    in_reply_to      = ToOneField(MessageResource, 'in_reply_to', null=True)
    class Meta:
        queryset = SubmissionEmailEvent.objects.all()
        serializer = api.Serializer()
        cache = SimpleCache()
        #resource_name = 'submissionemailevent'
        ordering = ['id', ]
        filtering = { 
            "id": ALL,
            "time": ALL,
            "desc": ALL,
            "msgtype": ALL,
            "submission": ALL_WITH_RELATIONS,
            "by": ALL_WITH_RELATIONS,
            "submissionevent_ptr": ALL_WITH_RELATIONS,
            "message": ALL_WITH_RELATIONS,
            "in_reply_to": ALL_WITH_RELATIONS,
        }
api.submit.register(SubmissionEmailEventResource())
