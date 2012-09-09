from unittest import TestCase, main
from runrunlib.footballsimulationinternals import process_state, \
                                                  _game_banner, \
                                                  _coin_flip, \
                                                  CoinFlipEvent
from runrunlib.footballsimulation import FootballSimulationGameState
from runrunlib import FootballTeam


class FootballSimulationInteralsTest(TestCase):
    pass


class CoinFlipTests(TestCase):
    def test_should_do_set_possession_if_time_is_zero(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .time(0) \
                    .quarter(1)

        # Act
        state2 = _coin_flip(state)

        # Assert
        self.assertTrue(state2.get_possession() in [teama, teamb])

    def test_should_skip_if_possession_is_set(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .possession(teamb)

        # Act
        state2 = _coin_flip(state)

        # Assert
        self.assertEqual(state2.get_possession(), teamb)

    def test_should_add_gameevent(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb)

        # Act
        state2 = _coin_flip(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], CoinFlipEvent)


if __name__ == '__main__':
    main()
