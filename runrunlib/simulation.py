from .gameresult import _FootballGameResult
from .simulationgamestate import FootballSimulationGameState
from .simulationsteps import pipeline as simulation_pipeline


def default_pipeline():
    for gamestage_pipeline in simulation_pipeline:
        for step in gamestage_pipeline:
            yield step


class FootballSimulationGame(object):
    def __init__(self, game):
        self._game = game

    def sim_game(self, pipeline=default_pipeline):
        state = FootballSimulationGameState() \
                    .gameid(self._game.get_gameid()) \
                    .team1(self._game.get_team1()) \
                    .team2(self._game.get_team2())

        for client in self._game.get_clients():
            state = state.add_client(client)

        for step in pipeline():
            state = step(state)

        return _FootballGameResult(self._game.get_team1())


class _FootballSimulationRunner(object):
    def run_game(self, game):
        simulation = FootballSimulationGame(game)
        return simulation.sim_game()


football_simulation = _FootballSimulationRunner()
