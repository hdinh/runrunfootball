from unittest import TestCase
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import FootballTeam


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

    def test_get_possession_should_be_not_set_at_constructor(self):
        # Arrange
        state = state = FootballSimulationGameState()

        # Assert
        self.assertFalse(state.get_possession().is_set())

    def test_get_team_should_be_not_set_at_constructor(self):
        # Arrange
        state = FootballSimulationGameState()

        # Assert
        self.assertFalse(state.get_team1().is_set())
        self.assertFalse(state.get_team2().is_set())

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

    def test_should_set_team1(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama'))

        # Assert
        self.assertEqual(state.get_team1().get_name(), 'teama')

    def test_should_set_team2(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .team2(FootballTeam('teamb'))

        # Assert
        self.assertEqual(state.get_team2().get_name(), 'teamb')

    def test_set_team1_should_throw_error_if_already_set(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama'))

        # Assert
        self.assertRaises(RuntimeError, state.team1, FootballTeam('another'))

    def test_set_team1_should_throw_error_if_already_set(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .team2(FootballTeam('teamb'))

        # Assert
        self.assertRaises(RuntimeError, state.team2, FootballTeam('another'))

    def test_should_set_possession(self):
        # Arrange & Act
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .possession(teama)

        # Assert
        self.assertEqual(state.get_possession(), teama)

    def test_set_possession_should_throw_error_if_team_not_1_or_2(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb)


        # Act & Assert
        self.assertRaises(RuntimeError, state.possession, FootballTeam('another'))

    def test_set_quarter_should_throw_error_if_out_of_range(self):
        # Arrange & Act
        state = FootballSimulationGameState()

        # Assert
        self.assertRaises(RuntimeError, state.quarter, -1)
        self.assertRaises(RuntimeError, state.quarter, 0)
        self.assertRaises(RuntimeError, state.quarter, 5)
