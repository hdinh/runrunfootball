from unittest import TestCase
from runrunlib.footballsimulationgamestate import FootballSimulationGameState


class FootballSimulationGameStateTests(TestCase):
    def test_get_time_at_constructor_should_be_zero(self):
        # Arrange
        state = state = FootballSimulationGameState()

        # Assert
        self.assertEqual(state.get_time(), 0)

    def test_get_quarter_at_constructor_should_be_zero(self):
        # Arrange
        state = state = FootballSimulationGameState()

        # Assert
        self.assertEqual(state.get_quarter(), 1)


    def test_should_set_time(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .time(138)

        # Assert
        self.assertEqual(state.get_time(), 138)

    def test_should_set_quarter(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .quarter(3)

        # Assert
        self.assertEqual(state.get_quarter(), 3)

    def test_set_quarter_should_throw_error_if_out_of_range(self):
        # Arrange & Act
        state = FootballSimulationGameState()

        # Assert
        self.assertRaises(RuntimeError, state.quarter, -1)
        self.assertRaises(RuntimeError, state.quarter, 0)
        self.assertRaises(RuntimeError, state.quarter, 5)
