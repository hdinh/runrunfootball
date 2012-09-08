from unittest import TestCase, skip
from runrunlib.footballsimulationinternals import process_state
from runrunlib.footballsimulation import FootballSimulationGameState
from runrunlib import FootballTeam


class FootballSimulationInteralsTest(TestCase):
    def test_prococess_state_should_do_coin_flip_if_initial(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .time(0) \
                    .quarter(1)

        # Act
        # Assert
