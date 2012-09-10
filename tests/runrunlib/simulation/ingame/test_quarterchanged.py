from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib.footballteam import FootballTeam
from runrunlib.simulation.ingame.gameloop import simulate_once
from runrunlib.simulation.ingame.quarterchanged import QuarterChangedEvent


class QuarterChangedTests(TestCase):
    def test_should_change_quarter_after_time_elapses_over_quarter_time(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(1) \
                    .quarter_time(40000) \
                    .time(40000)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertTrue(QuarterChangedEvent in map(lambda e: type(e), state2.get_events()))

    def test_should_not_change_quarter_after_time_elapses_over_quarter_time(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(1) \
                    .quarter_time(1000) \
                    .time(1)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertFalse(QuarterChangedEvent in map(lambda e: type(e), state2.get_events()))


if __name__ == '__main__':
    main()
