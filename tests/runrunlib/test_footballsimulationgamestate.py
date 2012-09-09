from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState, \
                                                  ViewOnlyFootballSimulationGameState
from runrunlib import FootballTeam, Event


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

    def test_get_nonpossession_should_be_not_set_at_constructor(self):
        # Arrange
        state = state = FootballSimulationGameState()

        # Assert
        self.assertFalse(state.get_nonpossession().is_set())

    def test_get_team_should_be_not_set_at_constructor(self):
        # Arrange
        state = FootballSimulationGameState()

        # Assert
        self.assertFalse(state.get_team1().is_set())
        self.assertFalse(state.get_team2().is_set())

    def test_get_events_should_be_zero_length_at_constructor(self):
        # Arrange
        state = FootballSimulationGameState()

        # Assert
        self.assertEqual(len(state.get_events()), 0)

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
        self.assertEqual(state.get_nonpossession(), teamb)

    def test_set_possession_should_throw_error_if_team_not_1_or_2(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb'))

        # Act & Assert
        self.assertRaises(RuntimeError, state.possession, FootballTeam('another'))

    def test_set_quarter_should_throw_error_if_out_of_range(self):
        # Arrange
        state = FootballSimulationGameState()

        # Assert
        self.assertRaises(RuntimeError, state.quarter, -1)
        self.assertRaises(RuntimeError, state.quarter, 0)

    def test_should_add_event(self):
        # Arrange & Act
        state = FootballSimulationGameState() \
                    .event(Event('my event 1')) \
                    .event(Event('second event'))

        # Assert
        self.assertEqual(state.get_events()[0].get_description(), 'my event 1')
        self.assertEqual(state.get_events()[1].get_description(), 'second event')

    def test_should_set_gameid(self):
        # Arrange & Act
        state = FootballSimulationGameState().gameid(100)

        # Assert
        self.assertEqual(state.get_gameid(), 100)

    def test_set_game_should_throw_error_if_already_set(self):
        # Arrange & Act
        state = FootballSimulationGameState().gameid(100)

        # Assert
        self.assertRaises(RuntimeError, state.gameid, 101)

    def test_should_set_quarter_count(self):
        # Arrange & Act
        state = FootballSimulationGameState().quarter_count(3)

        # Assert
        self.assertEqual(state.get_quarter_count(), 3)

    def test_should_set_quarter_time(self):
        # Arrange & Act
        state = FootballSimulationGameState().quarter_time(300)

        # Assert
        self.assertEqual(state.get_quarter_time(), 300)

    def test_get_view_only_state(self):
        # Arrange & Act
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .gameid(40) \
                    .team1(teama) \
                    .team2(teamb) \
                    .possession(teama) \
                    .quarter_count(4) \
                    .quarter(3) \
                    .quarter_time(300) \
                    .time(100) \
                    .get_view_only_state()

        # Assert
        self.assertEqual(state.get_gameid(), 40)
        self.assertEqual(state.get_team1().get_name(), 'teama')
        self.assertEqual(state.get_team2().get_name(), 'teamb')
        self.assertEqual(state.get_possession().get_name(), 'teama')
        self.assertEqual(state.get_nonpossession().get_name(), 'teamb')
        self.assertFalse(hasattr(state.get_team1(), 'get_controller'))
        self.assertFalse(hasattr(state.get_team2(), 'get_controller'))
        self.assertFalse(hasattr(state.get_possession(), 'get_controller'))
        self.assertFalse(hasattr(state.get_nonpossession(), 'get_controller'))
        self.assertEqual(state.get_quarter_count(), 4)
        self.assertEqual(state.get_quarter(), 3)
        self.assertEqual(state.get_quarter_time(), 300)
        self.assertEqual(state.get_time(), 100)
        self.assertIsInstance(state, ViewOnlyFootballSimulationGameState)


if __name__ == '__main__':
    main()
