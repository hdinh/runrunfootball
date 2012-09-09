from .kickoff import kickoff
from runrunlib.event import Event

pipeline = (kickoff,)

"""
pipeline = (kickoff,
            quarter(1),
            quarter_finished,
            quarter(2),
            halftime,
            kickoff,
            quarter(3),
            quarter_finished,
            quarter(4),
            game_finished)
"""

class FootballPlayOutcomeEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)
