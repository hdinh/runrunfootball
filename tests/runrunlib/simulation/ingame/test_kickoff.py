from unittest import TestCase, main
from runrunlib.simulation.ingame.kickoff import kickoff, \
                                                KickOffEvent
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import FootballTeam

class KickoffTests(TestCase):
    def test_should_kickoff_event(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb'))

        # Act
        state2 = kickoff(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], KickOffEvent)


if __name__ == '__main__':
    main()
