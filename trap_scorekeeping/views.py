"""trap_scorekeeping Views."""

from django.shortcuts import render
from . import logic
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


def render_score_input(request):
    """renders the score entry page"""
    template_data = {
        'things': 'stuff'
    }
    return render(request,
                  'trap_scorekeeping/score_entry.html',
                  template_data)