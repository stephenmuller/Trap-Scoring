"""trap_scorekeeping Models."""

from django.contrib.auth.models import User
from django.db import models
import string
from django.utils import timezone
import datetime


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


class SinglesScore(models.Model):
    """stores the scoring for a singles round"""
    score = models.CharField(max_length=25, default='', blank=True)
    score_type = models.BooleanField(default=True)

    def __repr__(self):
        """repr

        >>> a = SinglesScore()
        >>> a
        SinglesScore('', True)
        """
        return 'SinglesScore({!r}, {!r})'.format(self.score, self.score_type)

    def __str__(self):
        """str

        >>> print(str(SinglesScore(score='abc')))
        22
        """
        return str(self.convert_to_int_score())

    def add_missed_target(self, target_number):
        """adds a letter representing a missed target

        >>> a = SinglesScore()
        >>> a.add_missed_target(25)
        >>> a.score
        'y'
        """
        values = {}
        for index, letter in enumerate(string.ascii_lowercase, 1):
            values[index] = letter
        self.score = self.score + values[target_number]

    def convert_to_int_score(self):
        """takes a score from the obscured value to an int

        >>> a = SinglesScore()
        >>> a.add_missed_target(25)
        >>> a.convert_to_int_score()
        24
        """
        possible_score = 25
        missed_targets = len(self.score)
        score = possible_score - missed_targets
        return score


class Round(models.Model):
    """Links together the various classes/information for one round"""
    player = models.ForeignKey(User)
    singles_round = models.ForeignKey(
        SinglesScore,
        on_delete=models.CASCADE,
        related_name='singles_score'
    )
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

    def __repr__(self):
        return 'Round({!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r}, {!r})'.format(
            self.player, self.singles_round, self.date, self.location, self.shotgun, self.shells, self.started_at, self.excuses
        )

    def __str__(self):
        return self.singles_round
