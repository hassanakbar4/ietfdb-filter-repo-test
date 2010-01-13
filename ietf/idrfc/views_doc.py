# Copyright (C) 2009-2010 Nokia Corporation and/or its subsidiary(-ies).
# All rights reserved. Contact: Pasi Eronen <pasi.eronen@nokia.com>
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
#  * Neither the name of the Nokia Corporation and/or its
#    subsidiary(-ies) nor the names of its contributors may be used
#    to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import re, os
from datetime import datetime, time
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from ietf.idtracker.models import InternetDraft, IDInternal, BallotInfo, DocumentComment
from ietf.idrfc.models import RfcIndex, DraftVersions
from ietf.idrfc.idrfc_wrapper import BallotWrapper, IdWrapper, RfcWrapper
from ietf.idrfc import markup_txt
from ietf import settings
from django.template import RequestContext
from django.template.defaultfilters import truncatewords_html
from ietf.idtracker.templatetags.ietf_filters import format_textarea, fill
from django.utils.decorators import decorator_from_middleware
from django.middleware.gzip import GZipMiddleware


def document_debug(request, name):
    r = re.compile("^rfc([0-9]+)$")
    m = r.match(name)
    if m:
        rfc_number = int(m.group(1))
        rfci = get_object_or_404(RfcIndex, rfc_number=rfc_number)
        doc = RfcWrapper(rfci)
    else:
        id = get_object_or_404(InternetDraft, filename=name)
        doc = IdWrapper(draft=id)
    return HttpResponse(doc.to_json(), mimetype='text/plain')

def _get_html(key, filename):
    f = None
    try:
        f = open(filename, 'rb')
        raw_content = f.read()
    except IOError:
        return ("Error; cannot read "+key, "")
    finally:
        if f:
            f.close()
    (c1,c2) = markup_txt.markup(raw_content)
    return (c1,c2)

def document_main_rfc(request, rfc_number):
    rfci = get_object_or_404(RfcIndex, rfc_number=rfc_number)
    doc = RfcWrapper(rfci)

    info = {}
    info['is_rfc'] = True
    (content1, content2) = _get_html(
        "rfc"+str(rfc_number)+",html", 
        os.path.join(settings.RFC_PATH, "rfc"+str(rfc_number)+".txt"))

    if doc.in_ietf_process() and doc.ietf_process.has_iesg_ballot():
        ballot = doc.ietf_process.iesg_ballot()
    else:
        ballot = None
        
    history = _get_history(doc)
            
    return render_to_response('idrfc/doc_main_rfc.html',
                              {'content1':content1, 'content2':content2,
                               'doc':doc, 'info':info, 'ballot':ballot,
                               'history':history},
                              context_instance=RequestContext(request));

@decorator_from_middleware(GZipMiddleware)
def document_main(request, name):
    r = re.compile("^rfc([0-9]+)$")
    m = r.match(name)
    if m:
        return document_main_rfc(request, int(m.group(1)))
    id = get_object_or_404(InternetDraft, filename=name)
    doc = IdWrapper(id) 
    
    info = {}
    stream_id = doc.stream_id()
    if stream_id == 2:
        stream = " (IAB document)"
    elif stream_id == 3:
        stream = " (IRTF document)"
    elif stream_id == 4:
        stream = " (Independent submission via RFC Editor)"
    elif doc.group_acronym():
        stream = " ("+doc.group_acronym().upper()+" WG document)"
    else:
        stream = " (Individual document)"
        
    if id.status.status == "Active":
        info['is_active_draft'] = True
        info['type'] = "Active Internet-Draft"+stream
    else:
        info['is_active_draft'] = False
        info['type'] = "Old Internet-Draft"+stream

    info['has_pdf'] = (".pdf" in doc.file_types())
    info['is_rfc'] = False
    
    (content1, content2) = _get_html(
        str(name)+","+str(id.revision)+",html",
        os.path.join(settings.INTERNET_DRAFT_PATH, name+"-"+id.revision+".txt"))

    if doc.in_ietf_process() and doc.ietf_process.has_iesg_ballot():
        ballot = doc.ietf_process.iesg_ballot()
    else:
        ballot = None

    versions = _get_versions(id)
    history = _get_history(doc)
            
    return render_to_response('idrfc/doc_main_id.html',
                              {'content1':content1, 'content2':content2,
                               'doc':doc, 'info':info, 'ballot':ballot,
                               'versions':versions, 'history':history},
                              context_instance=RequestContext(request));

# doc is either IdWrapper or RfcWrapper
def _get_history(doc):
    results = []
    if doc.is_id_wrapper:
        comments = DocumentComment.objects.filter(document=doc.tracker_id)
    else:
        # note: DocumentComment.rfc_flag is often wrong; avoid it
        comments = DocumentComment.objects.filter(document=doc.rfc_number) 
    for comment in comments.order_by('-date','-time','-id').filter(public_flag=1).select_related('created_by'):
        info = {}
        info['text'] = comment.comment_text
        info['by'] = comment.get_fullname()
        info['textSnippet'] = truncatewords_html(format_textarea(fill(info['text'], 80)), 25)
        info['snipped'] = info['textSnippet'][-3:] == "..."
        results.append({'comment':comment, 'info':info, 'date':comment.datetime(), 'is_com':True})
    if doc.is_id_wrapper:
        versions = _get_versions(doc._draft, False)
        versions.reverse()
        for v in versions:
            v['is_rev'] = True
            results.append(v)
    if doc.is_id_wrapper and doc.draft_status == "Expired" and doc._draft.expiration_date:
        results.append({'is_text':True, 'date':doc._draft.expiration_date, 'text':'Draft expired'})
    if doc.is_rfc_wrapper:
        results.append({'is_text':True, 'date':doc.publication_date, 'text':'RFC Published'})

    # convert plain dates to datetimes (required for sorting)
    for x in results:
        if not isinstance(x['date'], datetime):
            x['date'] = datetime.combine(x['date'], time(0,0,0))

    results.sort(key=lambda x: x['date'])
    results.reverse()
    return results

# takes InternetDraft instance
def _get_versions(draft, include_replaced=True):
    ov = []
    ov.append({"draft_name":draft.filename, "revision":draft.revision_display(), "date":draft.revision_date})
    if include_replaced:
        draft_list = [draft]+list(draft.replaces_set.all())
    else:
        draft_list = [draft]
    for d in draft_list:
        for v in DraftVersions.objects.filter(filename=d.filename).order_by('-revision'):
            if (d.filename == draft.filename) and (draft.revision_display() == v.revision):
                continue
            ov.append({"draft_name":d.filename, "revision":v.revision, "date":v.revision_date})
    return ov

def document_ballot(request, name):
    r = re.compile("^rfc([0-9]+)$")
    m = r.match(name)
    if m:
        id = get_object_or_404(IDInternal, rfc_flag=1, draft=int(m.group(1)))
    else:
        id = get_object_or_404(IDInternal, rfc_flag=0, draft__filename=name)
    try:
        if not id.ballot.ballot_issued:
            raise Http404
    except BallotInfo.DoesNotExist:
        raise Http404

    ballot = BallotWrapper(id)
    return render_to_response('idrfc/doc_ballot.html', {'ballot':ballot}, context_instance=RequestContext(request))

