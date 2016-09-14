"""trap_scorekeeping Logic."""

from django.db import migrations, models
from .models import Round
from . import models
from django.db.models import Q
import string


def last_five_rounds():
    """querys for the last five rounds and returns a list

    """
    return Round.objects.all()[::-1][:5]


def players_last_ten(player_name):
    """returns last 10 rounds"""
    return Round.objects.filter(player__username=player_name)[::-1][:10]


def all_rounds_for_player(player_name):
    """returns all rounds for a given player"""
    return Round.objects.filter(player__username=player_name).select_related('singles_round')


def list_of_raw_scores(all_rounds):
    """Takes a query obj and spits out just the scores"""
    return [round_obj.singles_round.score for round_obj in all_rounds]


def dict_of_misses(raw_scores):
    split_scores = [list(score) for score in raw_scores]
    target_hit_miss_values = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        target_hit_miss_values[letter] = 0
    for single_round in split_scores:
        for target in single_round:
            target_hit_miss_values[target] += 1
    return target_hit_miss_values


def calculate_hit_rate(target_number_to_misses, missed_targets):
    """calculates the hit percentage for each target"""
    round_count = len(missed_targets)
    hit_ratios = {}
    for target in target_number_to_misses:
        if target != 0:
            hit_rate = target_number_to_misses[target]/round_count
        else:
            hit_rate = 1
        hit_ratios.update({target:hit_rate})
    return hit_ratios


def calculate_hit_percentages(hit_rate_by_target_id):
    """Takes ratios and converts them to percent values for display"""
    hit_percentages = {}
    for target in hit_rate_by_target_id:
        if hit_rate_by_target_id[target] == 0:
            hit_percentages.update({target:100})
        else:
            hit_percentages.update({target: 100 * hit_rate_by_target_id[target]})
    return hit_percentages


def avg_score_by_target(player_name):
    """calculates the average hit percentage by target"""
    all_rounds = all_rounds_for_player(player_name)
    raw_scores = list_of_raw_scores(all_rounds)
    misses = dict_of_misses(raw_scores)
    hit_rate = calculate_hit_rate(misses, raw_scores)
    hit_percentages = calculate_hit_percentages(hit_rate)
    return hit_percentages
