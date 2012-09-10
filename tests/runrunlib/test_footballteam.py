from unittest import TestCase, main
from unittest.mock import Mock
from runrunlib.footballteamcontroller import FootballTeamController
from runrunlib.footballteam import not_set_team, \
                                   FootballTeam, \
                                   ViewOnlyFootballTeam
from runrunlib.footballplaybook import FootballPlaybook, \
                                       default_playbook


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

    def test_controller_should_be_cpu_at_constructor(self):
        # Arrange & Act
        team = FootballTeam()

        # Assert
        self.assertTrue(team.get_controller().is_set())

    def test_unset_team_should_have_name_unset(self):
        # Assert
        self.assertEqual(not_set_team.get_name(), 'NotSet')
        self.assertFalse(not_set_team.is_set())

    def test_should_set_controller(self):
        # Arrange & Act
        controller = Mock(spec=FootballTeamController)
        team = FootballTeam() \
                .controller(controller)

        # Assert
        self.assertEqual(team.get_controller(), controller)

    def test_get_view_only_team(self):
        # Arrange & Act
        controller = Mock(spec=FootballTeamController)
        team = FootballTeam() \
                .name('team123') \
                .controller(controller) \
                .get_view_only_team()

        # Assert
        self.assertEqual(team.get_name(), 'team123')
        self.assertFalse(hasattr(team, 'get_controller'))

    def test_should_set_playbook(self):
        # Arrange & Act
        playbook = FootballPlaybook()
        team = FootballTeam() \
                .playbook(playbook)

        # Assert
        self.assertEqual(team.get_playbook(), playbook)

    def test_should_have_default_playbook_at_constructor(self):
        # Arrange & Act
        team = FootballTeam()

        # Assert
        self.assertEqual(team.get_playbook(), default_playbook)


if __name__ == '__main__':
    main()
