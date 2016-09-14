"""trap_scorekeeping Logic."""

from django.db import migrations, models
from .models import Round
from . import models
from django.db.models import Q
import string


def create_new_gun_model(brand, model, gauge, barrel_length, modifications):
    """creates a new database instance of the shotgun model

    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> models.Shotgun.objects.all()
    <QuerySet [Shotgun('beretta', 'a400', '12', 28, 'shell catcher')]>
    """
    new_shotgun = models.Shotgun(brand=brand, model=model, gauge=gauge, barrel_length=barrel_length,
                                 modifications= modifications
                                 )
    new_shotgun.save()


def create_new_shells_model(brand, sku, shot, shot_amount, fps_rating):
    """ creates a new database instance of the shells model

    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> models.Shells.objects.all()
    <QuerySet [Shells('remmington','gameloads','7.5''1oz',1290)]>
    """
    new_shells = models.Shells(brand=brand, sku=sku, shot_amount=shot_amount, fps_rating=fps_rating)
    new_shells.save()


def create_new_singles_score_from_misses(missed_target_ids):
    """creates a new instance of the singles_score class using missed target numbers

    >>> create_new_singles_score_from_misses([1, 2, 3])
    >>> models.SinglesScore.objects.all()
    <QuerySet [SinglesScore('abc', True)]>
    """
    new_score = models.SinglesScore()
    for target_id in missed_target_ids:
        new_score.add_missed_target(target_id)
    new_score.save()


def create_new_singles_score_from_int(score_as_int):
    """ Allows for the input of scores using just an integer value EG 23 (of 25), sets the flag to false because it doesn't
    provide sufficient data for missed targets in certain metrics.

    >>> create_new_singles_score_from_int(24)
    >>> models.SinglesScore.objects.all()
    <QuerySet [SinglesScore('a', False)]>

    >>> create_new_singles_score_from_int(25)
    >>> models.SinglesScore.objects.all()
    <QuerySet [SinglesScore('a', False), SinglesScore('', True)]>

    >>> create_new_singles_score_from_int(20)
    >>> models.SinglesScore.objects.all()
    <QuerySet [SinglesScore('a', False), SinglesScore('', True), SinglesScore('aaaaa', False)]>

    """
    if score_as_int == 25:
        new_score = models.SinglesScore()
        new_score.save()
    else:
        targets_missed = 25 - score_as_int
        score = 'a' * targets_missed
        new_score = models.SinglesScore(score=score, score_type=False)
        new_score.save()


def create_new_round(player, round_score, time, location_string, shotgun_model, shell_model, starting_station, excuses):
    """ creates and saves a new instance of the Round Model

    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(
    ... 'stephen', 24, time=datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club',
    ... models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1', 'no excuses!!')
    """
    new_round = models.Round(
        player=player, singles_round=validate_round_type(round_score), time='', location=location_string, shotgun=

    )


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

