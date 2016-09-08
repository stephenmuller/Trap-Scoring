"""trap_scorekeeping Models."""

from django.db import models
import string


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
    brand = models.TextField()
    model = models.TextField()
    gauge = models.ForeignKey(Gauge, related_name='shotgun_gauge')
    barrel_length = models.TextField()
    modifications = models.TextField()

    def __repr__(self):
        """repr"""
        return 'Player({!r},{!r},{!r})'.format(self.brand, self.model, self.gauge, self.modifications)

    def __str__(self):
        """basic defining characteristic"""
        return self.model


class Shells(models.Model):
    """Various information about shells, doesn't account for hand loads"""
    brand = models.TextField()
    sku = models.TextField()
    shot_weight = models.TextField()
    shot_size = models.TextField()
    dram_equivalent = models.TextField()
    fps_rating = models.TextField()
    gauge = models.ForeignKey(Gauge, related_name='shell_gauge')





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
    player = 'stephen'  # temporarily fixed until accounts are added
    singles_round = models.OneToOneField(
        SinglesScore,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date = models.DateTimeField(auto_now_add=True)  # can be used to pull weather later
    starting_station = 1  # the default station is one, small detail only useful for statistics
    location = 'Portland Gun Club'  # static for now, eventually will use the day class for this information
    shells = models.ForeignKey(Shells)

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r})'.format(
            self.singles_round, self.player, self.date, self.starting_station
        )

