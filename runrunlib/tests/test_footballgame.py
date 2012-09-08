import unittest
from runrunlib import FootballGame, FootballTeam


class FootballGameTests(unittest.TestCase):
    def test_name_should_set_name(self):
        game = FootballGame().gameid(40)
        self.assertEqual(game.get_gameid(), 40)
