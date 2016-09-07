"""A class for storing basic player information

'gun' will eventually be a class for storing things like make/model, barrel information, chokes etc.
"""

from django.db import models


class Player(models.Model):
    """Stores re-occurring player data"""
    name = models.TextField()
    gun = 'Beretta a400 Xplor Unico' # placeholder gun
    shells = 'shells placeholder'

    def __eq__(self, other):
        """eq"""
        Return(
            self.name == other.name and
            self.gun == other.gun and
            self.shells == other.shells
        )

    def __repr__(self):
        """repr

        >>> a = Player()
        >>> a
        >>> a
        """
        return 'Player({!r},{!r},{!r})'.format(self.name, self.gun, self.shells)

    def __str__(self):
        return self.name
