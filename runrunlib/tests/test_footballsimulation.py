from unittest import TestCase, skip
from runrunlib.footballsimulation import FootballGameSimulation
from runrunlib import FootballGame, FootballTeam


class FootballGameSimulationTests(TestCase):
    @skip("will do gameinternals first")
    def test_shit(self):
        # Arrange
        team1 = FootballTeam('team1')
        team2 = FootballTeam('team2')
        simulation = FootballGameSimulation(team1, team2)
        
        # Act
        game_result = simulation.sim_game()

        # Assert
