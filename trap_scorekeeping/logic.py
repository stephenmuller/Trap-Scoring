"""trap_scorekeeping Logic."""

from django.db import migrations, models
from .models import Round
from . import models
from django.db.models import Q


def last_five_rounds():
    """querys for the last five rounds and returns a list"""
    return Round.objects.all()[::-1][:5]


def players_last_ten(player_name):
    """returns last 10 rounds"""
    return Round.objects.filter(player__username=player_name)[::-1][:10]


# def avg_score_by_target(player_name):
#     """calculates the average hit percentage by target"""
#     all_rounds = all_rounds_for_player(player_name)
#     un_obfuscated_rounds = query_for_raw_scrores(all_rounds)
#     return averages


def all_rounds_for_player(player_name):
    """returns all rounds for a given player"""
    return Round.objects.filter(player__username=player_name).select_related('singles_round')


def query_for_raw_scrores(rounds_array):
    return [models.SinglesScore.objects.get(score_id)
        for score_id
        in rounds_array
    ]
