"""trap_scorekeeping Logic."""

from django.db import models
from . import models, dbinit
import string
from django.contrib.auth.models import User
import math


def make_giant_scores_list(scores):
    """takes all rounds and makes them into a giant true/false list

    >>> a = ['abc', 'y']
    >>> make_giant_scores_list(a)
    [False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False]
    """
    mega_score_list = []
    for round in scores:
        # convert string to list of missed targets
        individual_misses = list(round)
        # convert letters to numerical values, subtracting one to match 0-24 indexing
        numerical_target_values = [models.LETTER_TO_NUMBER_FOR_TARGET_MISSES[target] - 1 for target in individual_misses]
        # generate list of 25 targets, default true
        boolean_array_for_scores = [True for i in range(0, 25)]
        for target in numerical_target_values:
            boolean_array_for_scores[target] = False
        mega_score_list = mega_score_list + boolean_array_for_scores
    return mega_score_list


def strip_scores_from_round_model(queryset):
    r"""takes in a query and returns a list of the scores it contains

    >>> dbinit.set_up_test_db()
    >>> strip_scores_from_round_model(models.Round.objects.all())
    ['abc', 'abc', 'abc', 'abc', 'abc']
    """
    return [obj.score for obj in list(queryset)]


def find_streaks_in_rounds(all_rounds_as_giant_boolean_list):
    """outputs all streaks in a given list of booleans

    >>> a = [False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
    ... True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
    ... True, True, True, True, True, True, True, True, True, True, True, True, True, True, False]
    >>> find_streaks_in_rounds(a)
    [0, 0, 46]

    >>> b = [False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
    ... True, True, True, True, False, True, True, True, False, True, True, True, True, True, True, True, True, True,
    ... True, True, True, True, True, True, True, True, True, True, True, True, True, True, False]
    >>> find_streaks_in_rounds(b)
    [0, 0, 18, 3, 23]
    """
    false_indexes = [
        i
        for i, x in enumerate(all_rounds_as_giant_boolean_list)
        if x == False
    ]
    streaks = [
        i2 - i1 - 1
        for i1, i2 in zip(false_indexes, false_indexes[1:])
    ]
    return streaks


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


def create_new_round(player, round_score, time, location_string, shotgun_model, shell_model, starting_station, excuses):
    r""" creates and saves a new instance of the Round Model

    >>> create_user('test', 'test', 'test')
    >>> create_new_gun_model('beretta', 'a400', '12', 28, 'shell catcher')
    >>> create_new_shells_model('remmington', 'gameloads', '7.5', '1oz', 1290)
    >>> create_new_round(User.objects.get(id=1), 'abcd', '1997-07-16T19:20:30+01:00',
    ... 'portland gun club', models.Shotgun.objects.get(id=1), models.Shells.objects.get(id=1), '1',
    ... 'no excuses!!')
    >>> models.Round.objects.get(id=1)
    Round(<User: test>, 'abcd', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')
    """
    new_round = models.Round(
        player=player, score=round_score, date=time, location=location_string,
        shotgun=shotgun_model, shells=shell_model, started_at=starting_station, excuses=excuses
    )
    new_round.save()


def last_five_rounds_for_user(username):
    """querys for the last five rounds and returns a list

    >>> dbinit.set_up_test_db()
    >>> len(last_five_rounds_for_user('test'))
    4
    >>> last_five_rounds_for_user('test')
    [Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]
    """
    rounds = models.Round.objects.filter(player__username=username)[::-1][:5]
    return rounds


def last_five_rounds():
    """querys for the last five rounds and returns a list

    >>> dbinit.set_up_test_db()
    >>> last_five_rounds()
    [Round(<User: test2>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]
    >>> len(last_five_rounds())
    5
    """
    rounds = models.Round.objects.all()[::-1][:5]
    return rounds


def players_last_ten(player_name):
    """returns last 10 rounds

    >>> dbinit.set_up_test_db()
    >>> players_last_ten('test')
    [Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]
    >>> len(players_last_ten('test'))
    4
    """
    return models.Round.objects.filter(player__username=player_name)[::-1][:10]


def all_rounds_for_player(player_name):
    """returns all rounds for a given player

    >>> dbinit.set_up_test_db()
    >>> all_rounds_for_player('test')
    <QuerySet [Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!'), Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')]>
    >>> len(all_rounds_for_player('test'))
    4
    """
    return models.Round.objects.filter(player__username=player_name)


def list_of_raw_scores(all_rounds):
    """Takes a query obj and spits out just the scores

    >>> dbinit.set_up_test_db()
    >>> list_of_raw_scores(models.Round.objects.all())
    ['abc', 'abc', 'abc', 'abc', 'abc']
    """
    return [round_obj.score for round_obj in all_rounds]


def dict_of_misses(raw_scores):
    """Makes a dictionary mapping target number to amount of times missed

    >>> a ={'x': 0, 'q': 0, 'g': 0, 'u': 0, 'h': 0, 'i': 0, 'p': 0, 'r': 0, 'w': 0, 's': 0, 'd': 0, 'm': 0, 'c': 5,
    ... 'v': 0, 'z': 0, 'o': 0, 't': 0, 'e': 0, 'j': 0, 'a': 5, 'n': 0, 'b': 5, 'k': 0, 'l': 0, 'y': 0, 'f': 0}
    >>> a == dict_of_misses(['abc', 'abc', 'abc', 'abc', 'abc'])
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

    >>> num_to_miss = {'a': 1, 'b': 5, 'c': 3, 'd': 6, 'e': 0}
    >>> missed = ['a', 'a', 'a', 'a', 'a', 'a']
    >>> results = {'a': 83.33333333333334, 'b': 16.666666666666664, 'c': 50.0, 'd': 0.0, 'e': 100.0}
    >>> results == calculate_hit_rate(num_to_miss, missed)
    True
    """
    round_count = len(missed_targets)
    hit_ratios = {}
    for target in target_number_to_misses:
        hit_rate = (round_count - target_number_to_misses[target]) / round_count
        hit_ratios.update({target: hit_rate * 100})
    return hit_ratios


# def calculate_hit_percentages(hit_rate_by_target_id):
#     """Takes ratios and converts them to percent values for display
#
#     >>> test_dict = {'l': 0.0, 's': 0.0, 'h': 0.0, 'u': 0.0, 'w': 0.5, 'm': 0.0, 'f': 0.0, 'o': 1.0, 'q': 0.0, 'k': 0.0,
#     ... 'p': 0.0, 'd': 0.0, 'b': 0.0, 'c': 0.0, 'i': 0.0, 't': 0.0, 'x': 0.0, 'a': 0.0, 'g': 0.0, 'z': 0.0, 'y': 0.0,
#     ... 'j': 0.0, 'v': 0.0, 'r': 1.0, 'n': 0.0, 'e': 0.0}
#     >>> test_output = {'n': 100, 'z': 100, 'l': 100, 'c': 100, 'e': 100, 'q': 100, 'o': 0, 'i': 100, 'b': 100, 't': 100,
#     ... 'x': 100, 'y': 100, 'f': 100, 'h': 100, 'r': 0, 'k': 100, 'm': 100, 'u': 100, 's': 100, 'a': 100, 'g': 100,
#     ... 'w': 50.0, 'p': 100, 'd': 100, 'v': 100, 'j': 100}
#     >>> test_output == calculate_hit_percentages(test_dict)
#     True
#     """
#     hit_percentages = {}
#     for target in hit_rate_by_target_id:
#         if hit_rate_by_target_id[target] == 0:
#             hit_percentages.update({target: 100})
#         elif hit_rate_by_target_id[target] == 1.0:
#             hit_percentages.update({target: 0})
#         else:
#             hit_percentages.update({target: 100 * hit_rate_by_target_id[target]})
#     return hit_percentages


def delete_round_by_id(model_id):
    """ deletes a model based on the ID passed through
    >>> dbinit.set_up_test_db()
    >>> delete_round_by_id(1)
    >>> models.Round.objects.get(id__exact=1)
    Traceback (most recent call last):
     ...
    trap_scorekeeping.models.DoesNotExist: Round matching query does not exist.
    """
    model = models.Round.objects.get(id__exact=model_id)
    model.delete()


def avg_score_by_target(player_name):
    """calculates the average hit percentage by target
    >>> dbinit.set_up_test_db()
    >>> test_out = {'k': 100, 'i': 100, 'w': 100, 'r': 100, 'n': 100, 'z': 100, 'e': 100, 'q': 100, 'm': 100, 't': 100,
    ... 's': 100, 'v': 100, 'c': 0, 'y': 100, 'l': 100, 'u': 100, 'f': 100, 'j': 100, 'o': 100, 'h': 100, 'd': 100,
    ... 'x': 100, 'g': 100, 'a': 0, 'b': 0, 'p': 100}
    >>> a = {'x': 100.0, 'r': 100.0, 'i': 100.0, 'q': 100.0, 'b': 0.0, 't': 100.0, 's': 100.0, 'n': 100.0, 'f': 100.0,
    ... 'k': 100.0, 'g': 100.0, 'm': 100.0, 'd': 100.0, 'e': 100.0, 'o': 100.0, 'j': 100.0, 'u': 100.0, 'h': 100.0,
    ... 'a': 0.0, 'z': 100.0, 'c': 0.0, 'y': 100.0, 'w': 100.0, 'p': 100.0, 'l': 100.0, 'v': 100.0}
    >>> a == avg_score_by_target('test')
    True
    """
    all_rounds = all_rounds_for_player(player_name)
    raw_scores = list_of_raw_scores(all_rounds)
    misses = dict_of_misses(raw_scores)
    hit_rate = calculate_hit_rate(misses, raw_scores)
    return hit_rate


def calculate_streak_by_user(username):
    """calculates the streaks for the provided user

    >>> dbinit.set_up_test_db()
    >>> calculate_streak_by_user('test')
    [0, 0, 22, 0, 0, 22, 0, 0, 22, 0, 0]
    """
    rounds = all_rounds_for_player(username)
    scores = strip_scores_from_round_model(rounds)
    score_list = make_giant_scores_list(scores)
    streaks = find_streaks_in_rounds(score_list)
    return streaks


def calculate_total_shots_for_user(username):
    """calculates how many shots are recorded for a user

    >>> dbinit.set_up_test_db()
    >>> calculate_total_shots_for_user('test')
    100
    """
    rounds = models.Round.objects.filter(player__username=username).count()
    total_shots = rounds * 25
    return total_shots


def calculate_total_shots():
    """calculates the amount of shots recorded in the db

    >>> dbinit.set_up_test_db()
    >>> calculate_total_shots()
    125
    """
    rounds = models.Round.objects.all().count()
    total_shots = rounds * 25
    return total_shots


def hit_percentage_for_user(username):
    """calculates the percentage of targets hit for a given user

    >>> dbinit.set_up_test_db()
    >>> hit_percentage_for_user('test')
    0.88

    """
    total_logged_targets = calculate_total_shots_for_user(username)
    rounds = all_rounds_for_player(username)
    scores = strip_scores_from_round_model(rounds)
    all_scores = make_giant_scores_list(scores)
    hits = all_scores.count(True)
    return hits / total_logged_targets


def calculate_streaks():
    """calculates the longest streak in the db

    >>> dbinit.set_up_test_db()
    >>> calculate_streaks()
    [0, 0, 22, 0, 0, 22, 0, 0, 22, 0, 0, 22, 0, 0]
    """
    rounds = models.Round.objects.all()
    scores = strip_scores_from_round_model(rounds)
    score_list = make_giant_scores_list(scores)
    streaks = find_streaks_in_rounds(score_list)
    return streaks
