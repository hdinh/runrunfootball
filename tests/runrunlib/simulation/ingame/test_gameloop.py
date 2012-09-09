from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import FootballTeam
from runrunlib.simulation.ingame.gameloop import simulate_until_end, \
                                                 QuarterStartEvent


class GameLoopTests(TestCase):
    def test_(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(3)

        # Act
        state2 = simulate_until_end(state)

        # Assert


if __name__ == '__main__':
    main()
