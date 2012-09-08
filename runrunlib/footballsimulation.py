from .footballgameresult import _FootballGameResult


class FootballGameSimulation(object):
    def __init__(self, team1, team2):
        self._team1 = team1
        self._team2 = team2
        self._state = _FootballGameSimulationState()

    def sim_game(self):
        return _FootballGameResult(self._team1)


class _FootballGameSimulationState(object):
    pass


class _FootballSimulationRunner(object):
    def run_game(self, team1, team2):
        simulation = FootballGameSimulation(team1, team2)
        return simulation.sim_game()


football_simulation = _FootballSimulationRunner()
