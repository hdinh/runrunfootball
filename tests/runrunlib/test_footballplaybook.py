from unittest import TestCase, main
from unittest.mock import Mock
from runrunlib.footballplaybook import FootballPlaybook
from runrunlib import KickOffPlay, \
                      NormalPlay, \
                      OffensePlay, \
                      DefensePlay, \
                      KickOffKickingPlay, \
                      KickOffReceivingPlay


class FootballPlaybookTests(TestCase):
    def test_should_set_name(self):
        # Arrange & Act
        playbook = FootballPlaybook() \
                    .name('MyPlaybook')

        # Assert
        self.assertEqual(playbook.get_name(), 'MyPlaybook')

    def test_name_should_be_unamed_at_constructor(self):
        # Act & Assert
        self.assertEqual(FootballPlaybook().get_name(), 'Unnamed Playbook')

    def test_add_offense_play_should_be_able_to_add(self):
        # Arrange
        play = Mock(spec=OffensePlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_offense_play(play)

        # Assert
        self.assertTrue(play in playbook.get_offense_plays())

    def test_remove_offense_play_be_able_to_remove(self):
        # Arrange
        play = Mock(spec=OffensePlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_offense_play(play) \
                    .remove_offense_play(play)

        # Assert
        self.assertFalse(play in playbook.get_offense_plays())

    def test_add_defense_play_should_be_able_to_add(self):
        # Arrange
        play = Mock(spec=DefensePlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_defense_play(play)

        # Assert
        self.assertTrue(play in playbook.get_defense_plays())

    def test_remove_defense_play_be_able_to_remove(self):
        # Arrange
        play = Mock(spec=DefensePlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_defense_play(play) \
                    .remove_defense_play(play)

        # Assert
        self.assertFalse(play in playbook.get_defense_plays())

    def test_add_kickoff_receiving_play_should_be_able_to_add(self):
        # Arrange
        play = Mock(spec=KickOffReceivingPlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_kickoff_receiving_play(play)

        # Assert
        self.assertTrue(play in playbook.get_kickoff_receiving_plays())

    def test_remove_kickoff_receiving_play_be_able_to_remove(self):
        # Arrange
        play = Mock(spec=KickOffReceivingPlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_kickoff_receiving_play(play) \
                    .remove_kickoff_receiving_play(play)

        # Assert
        self.assertFalse(play in playbook.get_kickoff_receiving_plays())

    def test_add_kickoff_kicking_play_should_be_able_to_add(self):
        # Arrange
        play = Mock(spec=KickOffKickingPlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_kickoff_kicking_play(play)

        # Assert
        self.assertTrue(play in playbook.get_kickoff_kicking_plays())

    def test_remove_kickoff_kicking_play_be_able_to_remove(self):
        # Arrange
        play = Mock(spec=KickOffKickingPlay)

        # Act
        playbook = FootballPlaybook() \
                    .add_kickoff_kicking_play(play) \
                    .remove_kickoff_kicking_play(play)

        # Assert
        self.assertFalse(play in playbook.get_kickoff_kicking_plays())


if __name__ == '__main__':
    main()
