"""trap_scorekeeping Views."""

from django import shortcuts


def render_index(request):
    """renders the site index"""
    return render(
        request,
        'trap_scorekeeping/index.html',

    )