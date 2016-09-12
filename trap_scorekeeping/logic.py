"""trap_scorekeeping Logic."""

from django.db import migrations, models
from .models import Round
from django.db.models import Q


def last_five_rounds():
    """querys for the last five rounds and returns a list"""
    return Round.objects.all()[::-1][:5]


def players_last_ten(player_name):
    """returns last 10 rounds"""
    return Round.objects.filter(player__username=player_name)[::-1][:10]


def avg_score_by_target(player_name):
    """calculates the average hit percentage by target"""
    all_rounds = all_rounds_for_player(player_name).values_list('singles_round', flat=True)
    # all_scores =
    return all_rounds



def all_rounds_for_player(player_name):
    """returns all rounds for a given player"""
    return Round.objects.filter(player__username=player_name)
