import unittest
from runrunlib import FootballTeam


class FootballTeamTest(unittest.TestCase):
    def test_constructor_should_set_name_to_notnamed(self):
        team = FootballTeam()
        self.assertEqual(team.get_name(), 'NotNamed')

    def test_name_should_set_name(self):
        team = FootballTeam().name('TeamName')
        self.assertEqual(team.get_name(), 'TeamName')
