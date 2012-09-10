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
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        controller = CpuFootballTeamController()
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .possession(teama) \
                    .quarter(1) \
                    .get_view_only_state()

        # Act
        play = controller.choose_play(KickOffPlay, state)

        # Assert
        self.assertIsInstance(play, KickOffPlay)

    def test_choose_play_should_handle_kickoffplay(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        controller = CpuFootballTeamController()
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .possession(teama) \
                    .quarter(1) \
                    .time(20) \
                    .get_view_only_state()

        # Act
        play = controller.choose_play(NormalPlay, state)

        # Assert
        self.assertIsInstance(play, NormalPlay)


if __name__ == '__main__':
    main()
