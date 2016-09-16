"""trap_scorekeeping Logic."""

from django.db import models
from .models import Round
from . import models
import string
from django.contrib.auth.models import User
import numpy


def find_streaks_in_rounds(all_rounds_as_giant_boolean_list):
    """outputs all streaks in a given list of booleans"""
    rounds_with_false_at_end = all_rounds_as_giant_boolean_list.append(False)
    rounds_with_false_at_beginning_and_end = rounds_with_false_at_end.insert(0, False)
    false_indexes = [
        i
        for i, x in enumerate(rounds_with_false_at_beginning_and_end)
        if x == False
    ]
    streaks = [
        i2 - i1
        for i1, i2 in zip(false_indexes, false_indexes[1:])
    ]
    return streaks


# def longest_streak(rounds):
#     """for a given set of rounds returns the longest streak of targets hit
#     """
#     scores_to_process = list_of_raw_scores(rounds)
#     streaks = [find_longest_streak_in_single_round(score) for score in scores_to_process]
#     highest_single_round_streak = max(streaks)
#
#
#
# def find_longest_streak_in_single_round(round):
#     """takes in one round and returns the longest streak
#
#     >>> find_longest_streak_in_single_round('ay')
#     23
#     >>> find_longest_streak_in_single_round('a')
#     24
#     >>> find_longest_streak_in_single_round('y')
#     24
#     >>> find_longest_streak_in_single_round('d')
#     21
#     >>> find_longest_streak_in_single_round('fjot')
#     5
#     >>> find_longest_streak_in_single_round('o')
#     14
#     >>> find_longest_streak_in_single_round('ft')
#     14
#     >>> find_longest_streak_in_single_round('t')
#     19
#     """
#     # convert string to list of missed targets
#     individual_misses = list(round)
#     # convert letters to numerical values, subtracting one to match 0-24 indexing
#     numerical_target_values = [models.LETTER_TO_NUMBER_FOR_TARGET_MISSES[target] - 1 for target in individual_misses]
#     # generate list of 25 targets, default true
#     boolean_array_for_scores = [True for i in range(0, 25)]
#     # set missed targets to false
#     for target in numerical_target_values:
#         boolean_array_for_scores[target] = False
#     for
#     print(boolean_array_for_scores)



def create_user(username, user_pw, email='default@default.com'):
    """creates a new user with the default django function

    >>> create_user('steve', 'stupiddjangopw1')
    >>> User.objects.all()
    <QuerySet [<User: steve>]>
    """
    User.objects.create_user(username, email, user_pw)


def return_ten_users():
    """returns list of users for the homepage list

    >>> create_user('steve', 'stupiddjangopw1')
    >>> create_user('dave', 'stupiddjangopw1')
    >>> create_user('hans', 'stupiddjangopw1')
    >>> create_user('matt', 'stupiddjangopw1')
    >>> create_user('anne', 'stupiddjangopw1')
    >>> return_ten_users()
    [<User: anne>, <User: matt>, <User: hans>, <User: dave>, <User: steve>]
    """
    return User.objects.all()[::-1][:10]


def create_new_gun_model(brand, model, gauge, barrel_length, modifications):
    """creates a new database instance of the shotgun model

    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> models.Shotgun.objects.all()
    <QuerySet [Shotgun('beretta', 'a400', '12', 28, 'shell catcher')]>
    """
    new_shotgun = models.Shotgun(brand=brand, model=model, gauge=gauge, barrel_length=barrel_length,
                                 modifications=modifications
                                 )
    new_shotgun.save()


def create_new_shells_model(brand, sku, shot, shot_amount, fps_rating):
    """ creates a new database instance of the shells model

    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> models.Shells.objects.all()
    <QuerySet [Shells('remmington', 'gameloads', '7.5', '1oz', 1290)]>
    """
    new_shells = models.Shells(brand=brand, sku=sku, shot=shot, shot_amount=shot_amount, fps_rating=fps_rating)
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


def validate_round_type(score):
    """defines how a round should be saved"""
    if type(score) == int:
        create_new_singles_score_from_int(score)
        return models.SinglesScore.objects.all()[::-1][0]
    else:
        create_new_singles_score_from_misses(score)
        return models.SinglesScore.objects.all()[::-1][0]


def create_new_round(player, round_score, time, location_string, shotgun_model, shell_model, starting_station, excuses):
    r""" creates and saves a new instance of the Round Model

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), 24, '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> models.Round.objects.get(id=1)
    Round(<User: test>, SinglesScore('a', False), datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')
    """
    new_round = models.Round(
        player=player, singles_round=validate_round_type(round_score), date=time, location=location_string,
        shotgun=shotgun_model, shells=shell_model, started_at=starting_station, excuses=excuses
    )
    new_round.save()


def last_five_rounds():
    """querys for the last five rounds and returns a list

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), 24, '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:32+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 21, 22, 23], '1997-07-16T19:21:10+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:31+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> last_five_rounds()
    [Round(<User: test>, SinglesScore('abe', True), datetime.datetime(1997, 7, 16, 18, 21, 31, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, SinglesScore('abuvw', True), datetime.datetime(1997, 7, 16, 18, 21, 10, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, SinglesScore('abc', True), datetime.datetime(1997, 7, 16, 18, 21, 32, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, SinglesScore('abc', True), datetime.datetime(1997, 7, 16, 18, 21, 33, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, SinglesScore('or', True), datetime.datetime(1997, 7, 16, 18, 22, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]
    >>> len(last_five_rounds())
    5
    """
    return Round.objects.all()[::-1][:5]


def players_last_ten(player_name):
    """returns last 10 rounds

    >>> create_user('test', 'test', 'test')
    >>> create_user('test2', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=2), 24, '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:32+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 21, 22, 23], '1997-07-16T19:21:10+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:38+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:37+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:36+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:35+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:34+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:22:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> len(players_last_ten('test'))
    10
    """
    return Round.objects.filter(player__username=player_name)[::-1][:10]


def all_rounds_for_player(player_name):
    """returns all rounds for a given player

    >>> create_user('test', 'test', 'test')
    >>> create_user('test2', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=2), 24, '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:32+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 21, 22, 23], '1997-07-16T19:21:10+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:38+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:37+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:36+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:35+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:34+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:22:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> len(all_rounds_for_player('test'))
    11
    >>> len(all_rounds_for_player('test2'))
    1
    """
    return Round.objects.filter(player__username=player_name).select_related('singles_round')


def list_of_raw_scores(all_rounds):
    """Takes a query obj and spits out just the scores

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:33+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 3], '1997-07-16T19:21:32+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 21, 22, 23], '1997-07-16T19:21:10+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), [1, 2, 5], '1997-07-16T19:21:31+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> create_new_round(User.objects.get(id=1), 24, '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> list_of_raw_scores(Round.objects.all())
    ['or', 'abc', 'abc', 'abuvw', 'abe']
    """
    return [round_obj.singles_round.score for round_obj in all_rounds if round_obj.singles_round.score_type == True]


def dict_of_misses(raw_scores):
    """Makes a dictionary mapping target number to amount of times missed

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> a ={'x': 0, 'q': 0, 'g': 0, 'u': 0, 'h': 0, 'i': 0, 'p': 0, 'r': 1, 'w': 0, 's': 0, 'd': 0, 'm': 0, 'c': 0, 'v': 0, 'z': 0, 'o': 1, 't': 0, 'e': 0, 'j': 0, 'a': 0, 'n': 0, 'b': 0, 'k': 0, 'l': 0, 'y': 0, 'f': 0}
    >>> a == dict_of_misses(list_of_raw_scores(Round.objects.all()))
    True
    """
    split_scores = [list(score) for score in raw_scores]
    target_hit_miss_values = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        target_hit_miss_values[letter] = 0
    for single_round in split_scores:
        for target in single_round:
            target_hit_miss_values[target] += 1
    return target_hit_miss_values


def calculate_hit_rate(target_number_to_misses, missed_targets):
    """calculates the hit percentage for each target

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), [15, 18], '1997-07-16T19:22:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> test_dict = {'l': 0.0, 's': 0.0, 'h': 0.0, 'u': 0.0, 'w': 0.0, 'm': 0.0, 'f': 0.0, 'o': 1.0, 'q': 0.0, 'k': 0.0, 'p': 0.0, 'd': 0.0, 'b': 0.0, 'c': 0.0, 'i': 0.0, 't': 0.0, 'x': 0.0, 'a': 0.0, 'g': 0.0, 'z': 0.0, 'y': 0.0, 'j': 0.0, 'v': 0.0, 'r': 1.0, 'n': 0.0, 'e': 0.0}
    >>> test_dict == calculate_hit_rate(dict_of_misses(list_of_raw_scores(Round.objects.all())), list_of_raw_scores(Round.objects.all()))
    True
    """
    round_count = len(missed_targets)
    hit_ratios = {}
    for target in target_number_to_misses:
        if target != 0:
            hit_rate = target_number_to_misses[target]/round_count
        else:
            hit_rate = 1
        hit_ratios.update({target: hit_rate})
    return hit_ratios


def calculate_hit_percentages(hit_rate_by_target_id):
    """Takes ratios and converts them to percent values for display

    >>> test_dict = {'l': 0.0, 's': 0.0, 'h': 0.0, 'u': 0.0, 'w': 0.5, 'm': 0.0, 'f': 0.0, 'o': 1.0, 'q': 0.0, 'k': 0.0, 'p': 0.0, 'd': 0.0, 'b': 0.0, 'c': 0.0, 'i': 0.0, 't': 0.0, 'x': 0.0, 'a': 0.0, 'g': 0.0, 'z': 0.0, 'y': 0.0, 'j': 0.0, 'v': 0.0, 'r': 1.0, 'n': 0.0, 'e': 0.0}
    >>> test_output = {'n': 100, 'z': 100, 'l': 100, 'c': 100, 'e': 100, 'q': 100, 'o': 0, 'i': 100, 'b': 100, 't': 100, 'x': 100, 'y': 100, 'f': 100, 'h': 100, 'r': 0, 'k': 100, 'm': 100, 'u': 100, 's': 100, 'a': 100, 'g': 100, 'w': 50.0, 'p': 100, 'd': 100, 'v': 100, 'j': 100}
    >>> test_output == calculate_hit_percentages(test_dict)
    True
    """

    hit_percentages = {}
    for target in hit_rate_by_target_id:
        if hit_rate_by_target_id[target] == 0:
            hit_percentages.update({target: 100})
        elif hit_rate_by_target_id[target] == 1.0:
            hit_percentages.update({target: 0})
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


