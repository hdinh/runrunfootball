import unittest
from runrunlib import FootballTeam


class FootballTeamTest(unittest.TestCase):
    def test_can_be_named(self):
        team = FootballTeam().name('TeamName')
        self.assertEqual(team.get_name(), 'TeamName')
