from .footballgameresult import _FootballGameResult
from .footballsimulationgamestate import FootballSimulationGameState


class FootballSimulationGame(object):
    def __init__(self, team1, team2):
        self._team1 = team1
        self._team2 = team2
        self._state = FootballSimulationGameState()

    def sim_game(self):
        return _FootballGameResult(self._team1)


class _FootballSimulationRunner(object):
    def run_game(self, team1, team2):
        simulation = FootballSimulationGame(team1, team2)
        return simulation.sim_game()


football_simulation = _FootballSimulationRunner()
