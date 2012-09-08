from .footballteam import not_set_team
from .footballsimulation import football_simulation
from .footballgameresult import _FootballGameResult


class FootballGame(object):
    def __init__(self,
                 gameid=-1,
                 team1=not_set_team,
                 team2=not_set_team,
                 simulation=football_simulation):
        self._gameid = gameid
        self._team1 = team1
        self._team2 = team2
        self._simulation = simulation

    def run(self):
        if not self._team1.is_set():
            raise RuntimeError('team 1 is not set')
        if not self._team2.is_set():
            raise RuntimeError('team 2 is not set')

        game_result = self._simulation.run_game(team1=self._team1, team2=self._team2)

        # TODO: Cheat on purpose until we get test
        return _FootballGameResult(self._team1)

    def gameid(self, gameid):
        return FootballGame(gameid=gameid,
                            team1=self._team1,
                            team2=self._team2,
                            simulation=self._simulation)

    def team1(self, team):
        if self._team1.is_set():
            raise RuntimeError('team 1 already set')
        return FootballGame(gameid=self._gameid,
                            team1=team,
                            team2=self._team2,
                            simulation=self._simulation)

    def team2(self, team):
        if self._team2.is_set():
            raise RuntimeError('team 2 already set')
        return FootballGame(gameid=self._gameid,
                            team1=self._team1,
                            team2=team,
                            simulation=self._simulation)

    def simulation(self, simulation):
        return FootballGame(gameid=self._gameid,
                            team1=self._team1,
                            team2=self._team2,
                            simulation=simulation)

    def get_gameid(self):
        return self._gameid

    def get_team1(self):
        return self._team1

    def get_team2(self):
        return self._team2

    def get_simulation(self):
        return self._simulation
