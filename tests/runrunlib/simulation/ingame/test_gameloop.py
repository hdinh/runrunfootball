from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import FootballTeam
from runrunlib.simulation.ingame.gameloop import simulate_once, \
                                                 simulate_until, \
                                                 simulate_until_end, \
                                                 QuarterStartEvent
from runrunlib.simulation.ingame.kickoff import KickOffEvent


class GameLoopTests(TestCase):
    def test_should_do_kickoff_at_quarter1_time0(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(1) \
                    .time(0)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertTrue(KickOffEvent in map(lambda e: type(e), state2.get_events()))

    def test_should_not_do_kickoff_at_quarter1_time1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(1) \
                    .time(1)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertFalse(KickOffEvent in map(lambda e: type(e), state2.get_events()))


if __name__ == '__main__':
    main()
