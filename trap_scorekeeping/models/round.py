# """Stores a single round"""
#
#
# from singles_score import SinglesScore
# from models/player import Player
# from django.db import models
#
#
#
#
# class Round(models.Model):
#     """Links together the various classes/information for one round"""
#     singles_round = SinglesScore()
#     player = player  # stores user specific data that is mostly static
#     date = models.DateTimeField(auto_now_add=True)  # can be used to pull weather later
#     starting_station = 1  # the default station is one, small detail only useful for statistics
#     location = 'Portland Gun Club' # static for now, eventually will use the day class for this information
#     shells = shells class
#
#     def __eq__(self, other):
#         return(
#             self.singles_round == other.singles_round and
#             self.player == other.player and
#             self.date == other.date and
#             self.starting_station == other.starting_station
#         )
#
#     def __repr__(self):
#         return 'Round({!r}{!r}{!r}{!r})'.format(
#             self.singles_round, self.player, self.date, self.starting_station
#         )
#
