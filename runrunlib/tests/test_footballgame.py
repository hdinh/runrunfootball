import unittest
from runrunlib import FootballGame, FootballTeam


class FootballGameTests(unittest.TestCase):
    def test_name_should_set_name(self):
        # Arrange & Act
        game = FootballGame().gameid(40)

        # Assert
        self.assertEqual(game.get_gameid(), 40)

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

    def test_should_set_not_set_players_at_constructor(self):
        # Arrange & Act
        game = FootballGame()

        # Assert
        self.assertFalse(game.get_team1().is_set())
        self.assertFalse(game.get_team1().is_set())
