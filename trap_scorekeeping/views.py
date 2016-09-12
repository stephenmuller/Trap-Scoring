"""trap_scorekeeping Views."""

from django.shortcuts import render


def render_index(request):
    """renders the site index"""
    return render(
        request,
        'trap_scorekeeping/index.html',

    )