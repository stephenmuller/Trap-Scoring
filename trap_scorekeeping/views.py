"""trap_scorekeeping Views."""

from django.shortcuts import render
from . import logic
from . import forms
from . import models
from django.contrib.auth.models import User


def render_index(request):
    """renders the site index"""
    last_5 = logic.last_five_rounds()
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


def render_score_entry(request):
    """renders the score entry page"""
    template_data = {
        'test': 'nope',
    }
    return render(request,
                  'trap_scorekeeping/score_entry.html',
                  template_data)

def render_round_entry(request):
    """renders the round entry page"""
    score_from_post = request.POST.getlist('target')
    score_in_model_format = ''.join(score_from_post)
    form = forms.NewScore(request.POST or None, initial={
        'singles_round': score_in_model_format
    })
    # form.fields['singles_round'] = score_in_model_format
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    template_data = {
        'form': form,
    }
    return render(request,
                  'trap_scorekeeping/round_entry.html',
                  template_data)