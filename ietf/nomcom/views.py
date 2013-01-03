 # -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils import simplejson

from ietf.nomcom.utils import get_nomcom_by_year, is_nomcom_member, \
                              is_nomcom_chair, HOME_TEMPLATE
from ietf.nomcom.decorators import member_required
from ietf.nomcom.forms import EditPublicKeyForm, NominateForm
from ietf.nomcom.models import Position


def index(request, year):
    nomcom = get_nomcom_by_year(year)
    home_template = '/nomcom/%s/%s' % (nomcom.group.acronym, HOME_TEMPLATE)
    template = render_to_string(home_template, {})
    return render_to_response('nomcom/index.html',
                              {'nomcom': nomcom,
                               'year': year,
                               'selected': 'index',
                               'template': template}, RequestContext(request))


@member_required(role='member')
def private_index(request, year):
    nomcom = get_nomcom_by_year(year)
    is_nomcom_member(request.user, nomcom)
    return render_to_response('nomcom/private_index.html',
                              {'nomcom': nomcom,
                               'year': year,
                               'selected': 'index'}, RequestContext(request))


@member_required(role='chair')
def private_merge(request, year):
    # TODO: complete merge nominations
    nomcom = get_nomcom_by_year(year)
    is_nomcom_member(request.user, nomcom)
    return render_to_response('nomcom/private_merge.html',
                              {'nomcom': nomcom,
                               'year': year,
                               'selected': 'merge'}, RequestContext(request))


def requirements(request, year):
    nomcom = get_nomcom_by_year(year)
    positions = nomcom.position_set.all()
    return render_to_response('nomcom/requirements.html',
                              {'nomcom': nomcom,
                               'positions': positions,
                               'year': year,
                               'selected': 'requirements'}, RequestContext(request))


def questionnaires(request, year):
    nomcom = get_nomcom_by_year(year)
    positions = nomcom.position_set.all()
    return render_to_response('nomcom/questionnaires.html',
                              {'nomcom': nomcom,
                               'positions': positions,
                               'year': year,
                               'selected': 'questionnaires'}, RequestContext(request))


@login_required
def nominate(request, year):
    nomcom = get_nomcom_by_year(year)
    message = None
    if request.method == 'POST':
        form = NominateForm(data=request.POST, nomcom=nomcom, user=request.user)
        if form.is_valid():
            form.save()
            message = ('success', 'Your nomination has been registered. Thank you for the nomination.')
    else:
        form = NominateForm(nomcom=nomcom, user=request.user)

    return render_to_response('nomcom/nominate.html',
                              {'form': form,
                               'message': message,
                               'nomcom': nomcom,
                               'year': year,
                               'selected': 'nominate'}, RequestContext(request))


@login_required
def comments(request, year):
    # TODO: complete to do comments
    nomcom = get_nomcom_by_year(year)
    return render_to_response('nomcom/comments.html',
                              {'nomcom': nomcom,
                               'year': year,
                               'selected': 'comments'}, RequestContext(request))


@member_required(role='chair')
def edit_publickey(request, year):
    nomcom = get_nomcom_by_year(year)
    is_nomcom_chair(request.user, nomcom)
    is_group_chair = nomcom.group.is_chair(request.user)
    if not is_group_chair:
        return HttpResponseForbidden("Must be group chair")

    message = ('warning', 'Previous data will remain encrypted with the old key')
    if request.method == 'POST':
        form = EditPublicKeyForm(request.POST,
                                 request.FILES,
                                 instance=nomcom,
                                 initial={'public_key': None})
        if form.is_valid():
            form.save()
            message = ('success', 'The public key has been changed')
    else:
        form = EditPublicKeyForm()

    return render_to_response('nomcom/edit_publickey.html',
                              {'form': form,
                               'group': nomcom.group,
                               'message': message}, RequestContext(request))


def ajax_position_text(request, position_id):
    try:
        position_text = Position.objects.get(id=position_id).initial_text
    except Position.DoesNotExist:
        position_text = ""

    result = {'text': position_text}

    json_result = simplejson.dumps(result)
    return HttpResponse(json_result, mimetype='application/json')
