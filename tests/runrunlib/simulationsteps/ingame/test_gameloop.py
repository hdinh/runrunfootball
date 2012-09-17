from unittest import TestCase, main
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib import KickOffPlay, KickOffPlayOutcome
from runrunlib.team import FootballTeam
from runrunlib.simulationsteps.ingame.gameloop import simulate_once


class GameLoopTests(TestCase):
    def test_should_do_kickoff_at_quarter1_time0(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .time(0)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertTrue(KickOffPlayOutcome in map(lambda e: type(e), state2.get_events()))

    def test_should_not_do_kickoff_at_quarter1_time1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .time(1)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertFalse(KickOffPlayOutcome in map(lambda e: type(e), state2.get_events()))


if __name__ == '__main__':
    main()
