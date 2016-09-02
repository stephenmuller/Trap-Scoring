"""Creates rounds and puts them in the day.py class"""

# imports
from round import Round
from day import Day
from singles_score import SinglesScore
from round import Round
from player import Player

def main():
    """main"""
    set_up_test_data()



def set_up_test_data():
    stephen = Player('Stephen Muller')
    stephen_first_round = Round(stephen)
    first_round_misses = [21]
    stephen_first_round.singles_round.missed_target(first_round_misses)
    stephen_first_round.print_score()
    stephen_second_round = Round(stephen)
    second_round_misses = [6, 14, 24]
    stephen_second_round.singles_round.missed_target(second_round_misses)
    stephen_second_round.print_score()



# how the program should flow
# generate player
# generate new round
# take in score for round
# save score somewhere




main()