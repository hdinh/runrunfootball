from .footballteam import FootballTeam, FootballTeamController
from .footballgame import FootballGame
from .event import Event


class FootballPlay(object):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession):
        self._quarter = quarter
        self._time = time
        self._possession = possession
        self._nonpossession = nonpossession

    def get_quarter(self):
        return self._quarter

    def get_time(self):
        return self._time

    def get_possession(self):
        return self._possession

    def get_nonpossession(self):
        return self._nonpossession


class KickOffPlay(FootballPlay):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession):
        FootballPlay.__init__(self,
                              quarter,
                              time,
                              possession,
                              nonpossession)


class NormalPlay(FootballPlay):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession):
        FootballPlay.__init__(self,
                              quarter,
                              time,
                              possession,
                              nonpossession)
