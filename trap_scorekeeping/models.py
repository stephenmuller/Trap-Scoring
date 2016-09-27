"""trap_scorekeeping Models."""

from django.contrib.auth.models import User
from django.db import models
import string
from django.utils import timezone
from . import logic, dbinit


def generate_letter_to_target_number_dict():
    """makes dict of letter:number comparisons

    >>> a = {'g': 7, 'i': 9, 'v': 22, 'x': 24, 'b': 2, 'd': 4, 't': 20, 'y': 25, 's': 19, 'e': 5, 'a': 1, 'w': 23, 'q': 17, 'm': 13, 'l': 12, 'o': 15, 'h': 8, 'r': 18, 'f': 6, 'p': 16, 'n': 14, 'u': 21, 'k': 11, 'j': 10, 'z': 26, 'c': 3}
    >>> a == generate_letter_to_target_number_dict()
    True
    """
    values = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        values[letter] = index
    return values


def generate_target_number_to_letter_dict():
    """ makes dict of number:letter comparisons

    >>> a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
    >>> a == generate_target_number_to_letter_dict()
    True
    """
    values = {}
    for index, letter in enumerate(string.ascii_lowercase, 1):
        values[index] = letter
    return values

## Constants
LETTER_TO_NUMBER_FOR_TARGET_MISSES = generate_letter_to_target_number_dict()
NUMBER_TO_LETTER_FOR_TARGET_MISSES = generate_target_number_to_letter_dict()
SHOTS_PER_ROUND = 25

class Shells(models.Model):
    """Various information about shells, doesn't account for hand loads"""
    brand = models.CharField(max_length=25)
    sku = models.CharField(max_length=25)
    SEVEN_AND_A_HALF = '7.5'
    EIGHT = '8'
    EIGHT_AND_A_HALF = '8.5'
    NINE = '9'
    SHOT_CHOICES = (
        (SEVEN_AND_A_HALF, '7.5 Shot'),
        (EIGHT, '8 Shot'),
        (EIGHT_AND_A_HALF, '8.5'),
        (NINE, '9')
    )
    shot = models.CharField(
        choices=SHOT_CHOICES,
        default=SEVEN_AND_A_HALF,
        max_length=255
    )
    SEVEN_EIGHTHS_OUNCE = '7/8'
    ONE_OUNCE = '1'
    ONE_AND_ONE_EIGHTH = '1 1/8'
    SHOT_AMOUNTS = (
        (SEVEN_EIGHTHS_OUNCE, '7/8oz'),
        (ONE_OUNCE, '1oz'),
        (ONE_AND_ONE_EIGHTH, '1 1/8oz')
    )
    shot_amount = models.CharField(
        choices=SHOT_AMOUNTS,
        default=ONE_OUNCE,
        max_length=255
    )
    fps_rating = models.IntegerField()

    def __repr__(self):
        """test repr

        >>> a = Shells(brand='test', sku='test sku', shot='7.5', shot_amount='7/8', fps_rating=1290)
        >>> a
        Shells('test', 'test sku', '7.5', '7/8', 1290)
        """
        return 'Shells({!r}, {!r}, {!r}, {!r}, {!r})'.format(self.brand, self.sku, self.shot,
                                                        self.shot_amount, self.fps_rating)

    def __str__(self):
        r"""str

        >>> print(str(Shells(brand='test', sku='test sku', shot='7.5', shot_amount='7/8', fps_rating=
        ... 1290)))
        test sku
        """
        return self.sku


class Shotgun(models.Model):
    """all of the useful information about a shotgun"""
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    barrel_length = models.IntegerField()
    TWELVE_GAUGE = '12'
    TWENTY_GAUGE = '20'
    TWENTY_EIGHT_GAUGE = '28'
    FOUR_HUNDRED_TEN_GAUGE = '410'
    GAUGE_CHOICES = (
        (TWELVE_GAUGE, '12 Gauge'),
        (TWENTY_GAUGE, '20 Gauge'),
        (TWENTY_EIGHT_GAUGE, '28 Gauge'),
        (FOUR_HUNDRED_TEN_GAUGE, '410 Gauge')
    )
    gauge = models.CharField(
        choices=GAUGE_CHOICES,
        default=TWELVE_GAUGE,
        max_length=255
    )
    modifications = models.TextField()

    def __repr__(self):
        """repr
        >>> a = Shotgun(brand='beretta', model='a400', gauge='12', barrel_length=28, modifications='shell catcher')
        >>> a
        Shotgun('beretta', 'a400', '12', 28, 'shell catcher')
        """
        return 'Shotgun({!r}, {!r}, {!r}, {!r}, {!r})'.format(self.brand, self.model, self.gauge, self.barrel_length,
                                                              self.modifications)

    def __str__(self):
        """basic defining characteristic

        >>> a = Shotgun(brand='beretta', model='a400', gauge='12', barrel_length=28, modifications='shell catcher')
        >>> str(a)
        'a400'
        """
        return self.model


class Round(models.Model):
    """Links together the various classes/information for one round"""
    player = models.ForeignKey(User)
    date = models.DateTimeField(default=timezone.now)  # can be used to pull weather later
    location = models.TextField(default='Portland Gun Club')
    shotgun = models.ForeignKey(Shotgun, related_name='gun')
    shells = models.ForeignKey(Shells, related_name='ammo')
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'
    STARTING_STATIONS = (
        (FIRST, 'Station 1'),
        (SECOND, 'Station 2'),
        (THIRD, 'Station 3'),
        (FOURTH, 'Station 4'),
        (FIFTH, 'Station 5')
    )
    started_at = models.CharField(
        choices=STARTING_STATIONS,
        default=FIRST,
        max_length=255
    )
    excuses = models.TextField(default='')
    score = models.CharField(max_length=25, default='', blank=True)

    def convert_to_int_score(self):
        """takes a score from the obscured value to an int

        >>> a = Round()
        >>> a.score = 'abc'
        >>> a.convert_to_int_score()
        22
        """
        missed_targets = len(self.score)
        score = SHOTS_PER_ROUND - missed_targets
        return score

    def missed_targets_as_int(self):
        """returns a rounds score as the indexes of missed targets

        >>> logic.create_user('steve', 'stupiddjangopw1')
        >>> d = User.objects.get(id=1)
        >>> a = Shotgun(brand='beretta', model='a400', gauge='12', barrel_length=28, modifications='shell catcher')
        >>> b = Shells(brand='test', sku='test sku', shot='7.5', shot_amount='7/8', fps_rating=1290)
        >>> c = Round(player=d, shotgun= a, shells=b, score='abcdy')
        >>> c.missed_targets_as_int()
        [1, 2, 3, 4, 25]
        """
        list_of_letter_values = list(self.score)
        list_of_target_indexes = [LETTER_TO_NUMBER_FOR_TARGET_MISSES[target_letter]
                                  for target_letter
                                  in list_of_letter_values]
        return list_of_target_indexes

    def __repr__(self):
        """repr

        >>> dbinit.set_up_test_db()
        >>> Round.objects.get(id__exact=1)
        Round(<User: test>, 'abc', datetime.datetime(1997, 7, 16, 18, 20, 30, tzinfo=<UTC>), 'portland gun club', Shotgun('beretta', 'a400', '12', 28, 'shell catcher'), Shells('remmington', 'gameloads', '7.5', '1oz', 1290), '1', 'no excuses!!')
        """
        return 'Round({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.player, self.score, self.date, self.location, self.shotgun, self.shells, self.started_at, self.excuses
        )

    def __str__(self):
        """str
        >>> dbinit.set_up_test_db()
        >>> print(Round.objects.get(id__exact=1))
        User 'test', shot a 22, at 'portland gun club', with Shotgun('beretta', 'a400', '12', 28, 'shell catcher') and Shells('remmington', 'gameloads', '7.5', '1oz', 1290).
        """
        return 'User {!r}, shot a {!r}, at {!r}, with {!r} and {!r}.'.format(self.player.username, self.convert_to_int_score(),
                                                                             self.location, self.shotgun, self.shells)