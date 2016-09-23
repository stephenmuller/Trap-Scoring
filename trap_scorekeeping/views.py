"""trap_scorekeeping Views."""

from django.shortcuts import render
from django.shortcuts import redirect
from . import logic
from . import forms
from . import models
from django.contrib.auth.models import User


def render_index(request):
    """renders the site index"""
    last_5 = logic.last_five_rounds()
    # set up the score as an int value that makes sense to a human
    for round_obj in last_5:
        round_obj.score = round_obj.convert_to_int_score()
    user_list = logic.return_ten_users()
    template_data = {
        'rounds': last_5,
        'sidebar_users': user_list
    }
    return render(
        request,
        'trap_scorekeeping/index.html',
        template_data
    )


def render_score_entry(request, model_id=None):
    """renders the score entry page"""
    template_data = {
        'id': model_id,
    }
    return render(request,
                  'trap_scorekeeping/score_entry.html',
                  template_data)

def render_round_entry(request):
    """renders the round entry page"""
    form = forms.NewScore(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('score_entry', model_id=instance.pk)
    template_data = {
        'form': form
    }
    return render(request,
                  'trap_scorekeeping/round_entry.html',
                  template_data)

def render_ack_entry(request, model_id=None):
    template_data = {
        'filler': 'data'
    }
    return render(request, 'trap_scorekeeping/ack_entry.html', template_data)