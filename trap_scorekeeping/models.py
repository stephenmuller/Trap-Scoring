"""trap_scorekeeping Models."""

from django.db import models


class Round(models.Model):
    """Links together the various classes/information for one round"""
    singles_round = SinglesScore()
    player = player  # stores user specific data that is mostly static
    date = models.DateTimeField(auto_now_add=True)  # can be used to pull weather later
    starting_station = 1  # the default station is one, small detail only useful for statistics
    location = 'Portland Gun Club' # static for now, eventually will use the day class for this information
    shells = shells class

    def __eq__(self, other):
        return (
            self.singles_round == other.singles_round and
            self.player == other.player and
            self.date == other.date and
            self.starting_station == other.starting_station and
            self.location == other.location and
            self.shells == other.shells
        )

    def __repr__(self):
        return 'Round({!r}{!r}{!r}{!r})'.format(
            self.singles_round, self.player, self.date, self.starting_station
        )


class Shotgun(models.Model):
    """all of the useful information about a shotgun"""
    brand = models.TextField()
    model = models.TextField()
    gauge = models.TextField()
    barrel_length = models.TextField()
    modifications = models.TextField()

    def __eq__(self, other):
        """eq"""
        Return(
            self.brand == other.brand and
            self.model == other.model and
            self.gauge == other.gauge and
            self.barrel_length == other.barrel_length and
            self.modifications == other.modifications
        )

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
    twelve_gauge = 12
    twenty_gauge = 20
    twenty_eight_gauge = 28
    four_hundred_ten_gauge = 410
    GAUGE_CHOICES = (
        (twelve_gauge, '12g'),
        (twenty_gauge, '20g'),
        (twenty_eight_gauge, '28g'),
        (four_hundred_ten_gauge, '410g'),
    )
    year_in_school = models.CharField(
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=twelve_gauge,
    )
