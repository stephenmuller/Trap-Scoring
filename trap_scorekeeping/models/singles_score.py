"""A basic class that holds the default value for one round of 25 targets. By default they're all set to true"""

class SinglesScore:
    """score is a boolean representation of 25 targets
    data_type is intended to represent the data entry style
    true = either 0/25 or the specific shots missed were recorded
    false = data entered with int and can't be used for some statistics (EG. 23/25 twice in a row isn't necessarily
    the same as missing 1/2 and 24/25 which would have a streak of 46.)

    """
    def __init__(self):
        self.score = [
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True,
            True, True, True, True, True
        ]
        self.data_type = True

    def __eq__(self, other):
        return self.score == other.score, self.data_type == other.data_type

    def __repr__(self):
        return 'Score({}, {})'.format(self.score, self.data_type)

    def score_as_int(self):
        """Takes the boolean score and returns an integer value

        >>> a = SinglesScore()
        >>> a.score_as_int()
        25
        """
        return self.score.count(True)

    def missed_target(self, array_of_misses):
        """For setting an array of values to false

        >>> a = SinglesScore()
        >>> a.missed_target([24])
        >>> print(a.score)
        [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
        ... True, True, True, True, True, True, False]
        """
        for target_number in array_of_misses:
            self.score[target_number] = False


    # def station_score(self, scores_out_of_five, first_`station):
    #     """
    #
    #     :param score_out_of_five: int value between 1 and 5 representing the score at a station, assumed
    #     :param station: station shot from
    #     :return:
    #
    #     >>> a.SinglesScore()
    #     >>> a.StationScore()
    #     """
