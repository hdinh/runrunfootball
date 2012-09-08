from unittest import TestCase
from runrunlib.footballsimulationgamestate import FootballSimulationGameState


class FootballSimulationGameStateTests(TestCase):
    def test_should_set_time(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .time(138)

        # Assert
        self.assertEqual(state.get_time(), 138)
