from .gameresult import _FootballGameResult
from .simulationgamestate import FootballSimulationGameState
from .simulationsteps import pipeline as simulation_pipeline


def default_pipeline():
    for gamestage_pipeline in simulation_pipeline:
        for step in gamestage_pipeline:
            yield step


class FootballSimulationGame(object):
    def __init__(self, team1, team2, clients):
        self._team1 = team1
        self._team2 = team2
        self._clients = clients

    def sim_game(self, pipeline=default_pipeline):
        state = FootballSimulationGameState()

        for client in self._clients:
            state = state.add_client(client)

        for step in pipeline():
            state = step(state)

        return _FootballGameResult(self._team1)


class _FootballSimulationRunner(object):
    def run_game(self, team1, team2, clients=()):
        simulation = FootballSimulationGame(team1, team2, clients)
        return simulation.sim_game()


football_simulation = _FootballSimulationRunner()
