from unittest import TestCase
from runrunlib.footballsimulation import FootballGameSimulation
from runrunlib import FootballGame, FootballTeam


class FootballGameSimulationTests(TestCase):
    def test_shit(self):
        # Arrange
        team1 = FootballTeam('team1')
        team2 = FootballTeam('team2')
        simulation = FootballGameSimulation(team1, team2)
