from unittest import TestCase, skip, main
from unittest.mock import Mock
from runrunlib import Event
from runrunlib.simulation import FootballSimulationGame
from runrunlib.game import FootballGame
from runrunlib.team import FootballTeam
from runrunlib.simulation import football_simulation
from runrunlib.gameclient import FootballGameClient


class FootballSimulationTests(TestCase):
    def test_should_pass_clients_to_run_game(self):
        # Arrange
        game = FootballGame() \
                .team1(FootballTeam('team1')) \
                .team2(FootballTeam('team2'))

        # Act
        football_simulation.run_game(game)


class FootballSimulationGameTests(TestCase):
    def test_should_call_pipeline_in_order(self):
        # Arragne
        class S: pass
        s = S()
        s.times = 0
        def step(s):
            s.times += 1
            return lambda state: state
        def mock_pipeline(): return [step(s), step(s), step(s), step(s)]

        game = FootballGame() \
                .team1(FootballTeam('team1')) \
                .team2(FootballTeam('team2'))

        simulation = FootballSimulationGame(game=game)

        # Act
        simulation.sim_game(pipeline=mock_pipeline)

        # Assert
        self.assertEqual(4, s.times)

    def test_should_call_client_if_pipeline_adds_an_event(self):
        # Arrange
        event1 = Event('event1')

        def mock_step1(state): return state.event(event1)
        def mock_pipeline(): yield mock_step1

        mock_client1 = Mock(spec=FootballGameClient)
        mock_client2 = Mock(spec=FootballGameClient)

        game = FootballGame() \
                .team1(FootballTeam('team1')) \
                .team2(FootballTeam('team2')) \
                .add_client(mock_client1) \
                .add_client(mock_client2)

        simulation = FootballSimulationGame(game=game)

        # Act
        simulation.sim_game(pipeline=mock_pipeline)

        # Assert
        mock_client1.on_event.assert_called_once_with(event1)
        mock_client2.on_event.assert_called_once_with(event1)

    def test_should_pass_certain_properties_to_gamestate(self):
        # Arrange
        teama = FootballTeam('team1')
        teamb = FootballTeam('team2')
        game = FootballGame() \
                .gameid(3847) \
                .team1(teama) \
                .team2(teamb)

        simulation = FootballSimulationGame(game=game)
        class State: pass

        def mock_step1(state):
            State.game_state = state
            return state
        def mock_pipeline(): yield mock_step1

        # Act
        game_result = simulation.sim_game(pipeline=mock_pipeline)

        # Assert
        self.assertEqual(3847, State.game_state.get_gameid())
        self.assertEqual(teama, State.game_state.get_team1())
        self.assertEqual(teamb, State.game_state.get_team2())


if __name__ == '__main__':
    main()
