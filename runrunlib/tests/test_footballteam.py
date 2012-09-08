from unittest import TestCase
from runrunlib import FootballTeam
from runrunlib.footballteam import not_set_team


class FootballTeamTests(TestCase):
    def test_constructor_should_set_name_to_notnamed(self):
        # Arrange & Act
        team = FootballTeam()

        # Assert
        self.assertEqual(team.get_name(), 'NotNamed')

    def test_name_should_set_name(self):
        # Arrange & Act
        team = FootballTeam().name('TeamName')

        # Assert
        self.assertEqual(team.get_name(), 'TeamName')

    def test_is_set_should_be_true_from_constructor(self):
        # Arrange & Act
        team = FootballTeam()

        # Assert
        self.assertTrue(team.is_set())

    def test_unset_team_should_have_name_unset(self):
        # Assert
        self.assertEqual(not_set_team.get_name(), 'NotSet')
        self.assertFalse(not_set_team.is_set())
