"""A class for storing basic information about a players shotgun"""

from django.db import models


class Shotgun(models.Model):
    """Stores re-occurring player data"""
    brand = models.TextField()
    model = models.TextField()
    gauge = models.TextField()
    modifications = models.TextField()

    def __eq__(self, other):
        """eq"""
        Return (
            self.brand == other.brand and
            self.model == other.model and
            self.gauge == other.gauge and
            self.modifications == other.modifications
        )

    def __repr__(self):
        """repr"""
        return 'Player({!r},{!r},{!r})'.format(self.brand, self.model, self.gauge, self.modifications)

    def __str__(self):
        """basic defining characteristic"""
        return self.model
