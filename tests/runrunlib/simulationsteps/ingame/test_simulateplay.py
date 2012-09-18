from unittest import TestCase, main
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib.team import FootballTeam
from runrunlib.simulationsteps.ingame.gameloop import simulate_once
from runrunlib import NormalPlayOutcome


class SimulateFootballPlayTests(TestCase):
    def test_should_simulate_play_if_time_elapses(self):
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
        self.assertIsInstance(state2.get_events()[-1], NormalPlayOutcome)
        #self.assertTrue(state2.get_time() - state.get_time() > 0)


if __name__ == '__main__':
    main()
