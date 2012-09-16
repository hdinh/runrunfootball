from unittest import TestCase, main
from runrunlib import KickOffPlay, NormalPlay
from runrunlib.footballteam import FootballTeam
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib.footballteamcontroller import not_set_controller, \
                                             FootballTeamController, \
                                             CpuFootballTeamController


class CpuFootballTeamControllerTests(TestCase):
    def test_choose_play_should_handle_kickoffplay(self):
        # Arrange
        controller = CpuFootballTeamController()
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .get_view_only_state()

        # Act
        play = controller.choose_play(KickOffPlay, state)

        # Assert
        self.assertIsInstance(play, KickOffPlay)

    def test_choose_play_should_handle_normalplay(self):
        # Arrange
        controller = CpuFootballTeamController()
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .time(20) \
                    .get_view_only_state()

        # Act
        play = controller.choose_play(NormalPlay, state)

        # Assert
        self.assertIsInstance(play, NormalPlay)

    def test_cpu_controller_is_set_should_be_true(self):
        # Act & Assert
        self.assertTrue(CpuFootballTeamController().is_set())

    def test_non_set_controller_is_set_should_be_true(self):
        # Act & Assert
        self.assertFalse(not_set_controller.is_set())

    def test_should_only_choose_play_from_playbook(self):
        # TODO
        pass


if __name__ == '__main__':
    main()
