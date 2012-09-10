from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import FootballTeam
from runrunlib.simulation.ingame.gameloop import simulate_once
from runrunlib import NormalPlayOutcome


class SimulateFootballPlayTests(TestCase):
    def test_should_simulate_play_if_time_elapses(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter_count(4) \
                    .quarter(1) \
                    .quarter_time(1000) \
                    .time(1)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], NormalPlayOutcome)
        #self.assertTrue(state2.get_time() - state.get_time() > 0)


if __name__ == '__main__':
    main()
