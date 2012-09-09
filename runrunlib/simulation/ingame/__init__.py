from .kickoff import kickoff

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
