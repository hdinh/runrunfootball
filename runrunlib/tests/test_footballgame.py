from unittest import TestCase
from unittest.mock import Mock
from runrunlib import FootballGame, FootballTeam
from runrunlib.footballteam import not_set_team
from runrunlib.footballlogic import football_logic


class FootballGameTests(TestCase):
    def test_name_should_set_name(self):
        # Arrange & Act
        game = FootballGame().gameid(40)

        # Assert
        self.assertEqual(game.get_gameid(), 40)

    def test_logic_should_be_set_to_football(self):
        # Arrange
        game = FootballGame()

        # Assert
        self.assertEqual(game.get_logic(), football_logic)

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

    def test_running_game_should_call_and_return_logic_rungame(self):
        # Arrange & Act
        mock_logic = Mock(spec=type(football_logic))
        team1 = FootballTeam(name='team1')
        team2 = FootballTeam(name='team2')

        # Act
        game_result = FootballGame() \
                        .team1(team1) \
                        .team2(team2) \
                        .logic(mock_logic) \
                        .run()

        # Assert
        mock_logic.run_game.assert_called_once_with(team1=team1, team2=team2)
