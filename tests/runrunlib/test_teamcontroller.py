from unittest import TestCase, main
from runrunlib.playbook import FootballPlaybook, default_playbook
from runrunlib.team import FootballTeam
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib.teamcontroller import not_set_controller, \
                                     FootballTeamController, \
                                     CpuFootballTeamController
from runrunlib import KickOffReceivingPlay, \
                      KickOffKickingPlay, \
                      OffensePlay, \
                      DefensePlay


class CpuFootballTeamControllerTests(TestCase):
    def test_choose_play_should_handle_kickoff_test(self):
        for play_klass in (KickOffReceivingPlay, KickOffKickingPlay):
            # Arrange
            controller = CpuFootballTeamController()
            playbook = default_playbook
            state = FootballSimulationGameState() \
                        .team1(FootballTeam('teama')) \
                        .team2(FootballTeam('teamb')) \
                        .possession_index(0) \
                        .quarter(1) \
                        .get_view_only_state()

            # Act
            play = controller.choose_play(KickOffReceivingPlay, state, playbook)

            # Assert
            self.assertIsInstance(play, KickOffReceivingPlay)

    def test_choose_play_should_handle_normal(self):
        for play_klass in (OffensePlay, DefensePlay):
            # Arrange
            controller = CpuFootballTeamController()
            playbook = default_playbook
            state = FootballSimulationGameState() \
                        .team1(FootballTeam('teama')) \
                        .team2(FootballTeam('teamb')) \
                        .possession_index(0) \
                        .quarter(1) \
                        .time(20) \
                        .get_view_only_state()

            # Act
            play = controller.choose_play(play_klass, state, playbook)

            # Assert
            self.assertIsInstance(play, play_klass)

    def test_cpu_controller_is_set_should_be_true(self):
        # Act & Assert
        self.assertTrue(CpuFootballTeamController().is_set())

    def test_non_set_controller_is_set_should_be_true(self):
        # Act & Assert
        self.assertFalse(not_set_controller.is_set())

    def test_should_only_choose_play_from_playbook(self):
        # Arrange
        controller = CpuFootballTeamController()
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .get_view_only_state()
        playbook = FootballPlaybook() \
                    .add_kickoff_kicking_play(KickOffKickingPlay().name('name1'))

        # Act
        play = controller.choose_play(KickOffKickingPlay, state, playbook)

        # Assert
        self.assertEqual('name1', play.get_name())


if __name__ == '__main__':
    main()
