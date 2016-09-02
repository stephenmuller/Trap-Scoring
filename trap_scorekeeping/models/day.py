"""Class for collecting the details relevent to a day"""

from django.db import models


class Day(models.Model):
    """Weather, wind, other"""
    weather = 'fetch weather'
    wind = 'fetch wind, potentially same source?'
    excuses = 'random excuses, eg was tired that day'

    def __eq__(self, other):
        return(
            self.weather == other.weather and
            self.wind == other.wind and
            self.excuses == other.excuses
        )

    def __repr__(self):
        return 'Day(weather={!r}, wind={!r}, excuses={!r})'.format(self.weather, self.wind, self.excuses)
