from unittest import TestCase, skip
from runrunlib.footballsimulation import FootballSimulationGame
from runrunlib import FootballGame, FootballTeam


class FootballSimulationGameTests(TestCase):
    @skip("will do gameinternals first")
    def test_shit(self):
        # Arrange
        team1 = FootballTeam('team1')
        team2 = FootballTeam('team2')
        simulation = FootballSimulationGame(team1, team2)
        
        # Act
        game_result = simulation.sim_game()

        # Assert
