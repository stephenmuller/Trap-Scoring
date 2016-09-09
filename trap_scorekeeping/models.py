"""trap_scorekeeping Models."""

from django.contrib.auth.models import User
from django.db import models
import string


class StartingStation(models.Model):
    """adds the ability to select a starting station"""
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

class ShotAmount(models.Model):
    """the standard shot amounts"""
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

    def __repr__(self):
        return 'ShotAmount({!r})'.format(self.shot_amount)

    def __str__(self):
        return self.shot_amount


class ShotSize(models.Model):
    """standard shot sizes"""
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

    def __repr__(self):
        return 'Shot({!r})'.format(self.shot)

    def __str__(self):
        return self.shot


class Gauge(models.Model):
    """contains the four major gauges"""
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

    def __repr__(self):
        return 'Gauge({!r})'.format(self.gauge)

    def __str__(self):
        return self.gauge


class Shotgun(models.Model):
    """all of the useful information about a shotgun"""
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=25)
    gauge = models.ForeignKey(Gauge, related_name='shotgun_gauge')
    barrel_length = models.IntegerField()
    modifications = models.TextField()

    def __repr__(self):
        """repr"""
        return 'Player({!r},{!r},{!r})'.format(self.brand, self.model, self.gauge, self.modifications)

    def __str__(self):
        """basic defining characteristic"""
        return self.model


class Shells(models.Model):
    """Various information about shells, doesn't account for hand loads"""
    brand = models.CharField(max_length=25)
    sku = models.CharField(max_length=25)
    shot_size = models.ForeignKey(ShotSize, related_name='size')
    shot_weight = models.ForeignKey(ShotAmount, related_name='weight')
    fps_rating = models.IntegerField()
    gauge = models.ForeignKey(Gauge, related_name='shell_gauge')

    def __repr__(self):
        return 'Shells({!r},{!r},{!r}{!r},{!r},{!r})'.format(self.brand, self.sku, self.shot_size,
                                                             self.shot_weight, self.fps_rating, self.gauge
                                                             )


class SinglesScore(models.Model):
    """stores the scoring for a singles round"""
    score = models.CharField(max_length=25, default='', blank=True)
    score_type = models.BooleanField(default=True)

    def __repr__(self):
        """repr

        >>> a = SinglesScore()
        >>> a
        'Score('', True)'
        """
        return 'SinglesScore({!r}, {!r})'.format(self.score, self.score_type)

    def __str__(self):
        return self.score

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
        POSSIBLE_SCORE = 25
        missed_targets = len(self.score)
        score = POSSIBLE_SCORE - missed_targets
        return score


class Round(models.Model):
    """Links together the various classes/information for one round"""
    player = models.ForeignKey(User)
    singles_round = models.OneToOneField(
        SinglesScore,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date = models.DateTimeField(auto_now_add=True)  # can be used to pull weather later
    starting_station = models.ForeignKey(ShotSize, related_name='first_station')
    location = 'Portland Gun Club'  # static for now, eventually will use the day class for this information
    shells = models.ForeignKey(Shells)

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r})'.format(
            self.singles_round, self.player, self.date, self.starting_station
        )


