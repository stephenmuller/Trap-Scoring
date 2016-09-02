"""Class for collecting the details relevent to a day"""

class Day:
    """Weather, wind, other"""
    def __init__(self):
        self.weather = 'fetch weather'
        self.wind = 'fetch wind, potentially same source?'
        self.other = 'random excuses, eg was tired that day'

    def __eq__(self, other):
        return(
            self.weather == other.weather and
            self.wind == other.wind and
            self.other == other.wind
        )