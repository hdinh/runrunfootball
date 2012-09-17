from .footballgameresult import _FootballGameResult
from .footballsimulationgamestate import FootballSimulationGameState
from .simulation import pipeline as simulation_pipeline


class FootballSimulationGame(object):
    def __init__(self, team1, team2, clients=()):
        self._team1 = team1
        self._team2 = team2
        self._clients = clients

    def sim_game(self):
        state = FootballSimulationGameState()

        for gamestage_pipeline in simulation_pipeline:
            for step in gamestage_pipeline:
                self._state = step(state)

        return _FootballGameResult(self._team1)


class _FootballSimulationRunner(object):
    def run_game(self, team1, team2, clients=()):
        simulation = FootballSimulationGame(team1, team2, clients)
        return simulation.sim_game()


football_simulation = _FootballSimulationRunner()
