from unittest import TestCase, skip, main
from unittest.mock import Mock
from runrunlib import Event
from runrunlib.footballsimulation import FootballSimulationGame
from runrunlib.footballgame import FootballGame
from runrunlib.footballteam import FootballTeam
from runrunlib.footballsimulation import football_simulation
from runrunlib.footballgameclient import FootballGameClient


class FootballSimulationTests(TestCase):
    def test_should_pass_clients_to_run_game(self):
        # Arrange & Act
        football_simulation.run_game(team1=FootballTeam('team1'),
                                     team2=FootballTeam('team2'),
                                     clients=())


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

        simulation = FootballSimulationGame(team1=FootballTeam('team1'),
                                            team2=FootballTeam('team2'),
                                            clients=())

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

        simulation = FootballSimulationGame(team1=FootballTeam('team1'),
                                            team2=FootballTeam('team2'),
                                            clients=(mock_client1, mock_client2))

        # Act
        simulation.sim_game(pipeline=mock_pipeline)

        # Assert
        mock_client1.on_event.assert_called_once_with(event1)
        mock_client2.on_event.assert_called_once_with(event1)

    def test_should_notify_events_to_clients(self):
        # Arrange
        simulation = FootballSimulationGame(team1=FootballTeam('team1'),
                                            team2=FootballTeam('team2'),
                                            clients=())

        # Act
        game_result = simulation.sim_game()

        # Assert
        return


if __name__ == '__main__':
    main()
