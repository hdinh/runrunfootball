from unittest import TestCase, main
from unittest.mock import Mock, ANY

from runrunlib.game import FootballGame
from runrunlib.team import not_set_team, FootballTeam
from runrunlib.simulation import football_simulation
from runrunlib.gameclient import FootballGameClient
from runrunlib.event import Event


class FootballGameTests(TestCase):
    def test_name_should_set_name(self):
        # Arrange & Act
        game = FootballGame().gameid(40)

        # Assert
        self.assertEqual(game.get_gameid(), 40)

    def test_simulation_should_be_set_to_football(self):
        # Arrange
        game = FootballGame()

        # Assert
        self.assertEqual(game.get_simulation(), football_simulation)

    def test_should_set_players_of_game(self):
        # Arrange & Act
        game = FootballGame() \
                .team1(FootballTeam(name='team356')) \
                .team2(FootballTeam(name='team861'))

        # Assert
        self.assertTrue(game.get_team1().is_set())
        self.assertTrue(game.get_team2().is_set())
        self.assertEqual(game.get_team1().get_name(), 'team356')
        self.assertEqual(game.get_team2().get_name(), 'team861')

    def test_team_should_set_notsettream_at_constructor(self):
        # Arrange & Act
        game = FootballGame()

        # Assert
        self.assertFalse(game.get_team1().is_set())
        self.assertFalse(game.get_team1().is_set())

    def test_team1_should_throw_exception_if_team_is_already_set(self):
        # Arrange
        game = FootballGame().team1(FootballTeam(name='team1'))

        # Act & Assert
        self.assertRaises(RuntimeError, game.team1, FootballTeam('another'))

    def test_team2_should_throw_exception_if_team_is_already_set(self):
        # Arrange
        game = FootballGame().team2(FootballTeam(name='team2'))

        # Act & Assert
        self.assertRaises(RuntimeError, game.team2, FootballTeam('another'))

    def test_run_should_throw_exception_if_team1_is_not_set(self):
        # Arrange
        game = FootballGame().team2(FootballTeam(name='team2'))

        # Act & Assert
        self.assertRaises(RuntimeError, game.run)

    def test_run_should_throw_exception_if_team2_is_not_set(self):
        # Arrange
        game = FootballGame().team1(FootballTeam(name='team1'))

        # Act & Assert
        self.assertRaises(RuntimeError, game.run)

    def test_running_game_should_declare_winner_at_end(self):
        # Arrange & Act
        game_result = FootballGame() \
                        .team1(FootballTeam(name='team1')) \
                        .team2(FootballTeam(name='team2')) \
                        .run()

        # Assert
        winner = game_result.get_winner()
        self.assertTrue(winner.get_name() == 'team1' or winner.get_name() == 'team2')

    def test_running_game_should_call_and_return_simulation_rungame(self):
        # Arrange & Act
        mock_simulation = Mock(spec=type(football_simulation))
        team1 = FootballTeam(name='team1')
        team2 = FootballTeam(name='team2')

        # Act
        game = FootballGame() \
                .team1(team1) \
                .team2(team2) \
                .simulation(mock_simulation)
        game_result = game.run()

        # Assert
        mock_simulation.run_game.assert_called_once_with(game)

    def test_add_client_should_return_client_when_get_clients(self):
        # Arrange
        mock_client = Mock(spec=FootballGameClient)

        # Act
        game = FootballGame() \
                .team1(FootballTeam(name='team1')) \
                .team2(FootballTeam(name='team2')) \
                .add_client(mock_client)

        # Assert
        self.assertTrue(mock_client in game.get_clients())

    def test_add_client_should_get_events_from_simulation(self):
        # Arrange
        event = Event('my event')
        def mock_run_game(game):
            for client in game.get_clients():
                client.on_event(event=event)

        mock_client = Mock(spec=FootballGameClient)
        mock_simulation = Mock(spec=type(football_simulation))
        mock_simulation.run_game = mock_run_game

        # Act
        game = FootballGame() \
                .team1(FootballTeam(name='team1')) \
                .team2(FootballTeam(name='team2')) \
                .simulation(mock_simulation) \
                .add_client(mock_client)
        game.run()

        # Assert
        mock_client.on_event.assert_called_once_with(event=event)


if __name__ == '__main__':
    main()
