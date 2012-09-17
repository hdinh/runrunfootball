from unittest import TestCase, main
from runrunlib.simulationsteps.pregame.coinflip import coin_flip, \
                                                  CoinFlipEvent
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib.team import FootballTeam


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
        state2 = coin_flip(state)

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
        state2 = coin_flip(state)

        # Assert
        self.assertEqual(state2.get_possession(), teamb)

    def test_should_add_coin_flip_event(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb'))

        # Act
        state2 = coin_flip(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], CoinFlipEvent)


