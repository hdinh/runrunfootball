from unittest import TestCase, skip, main
from runrunlib.footballsimulation import FootballSimulationGame
from runrunlib.footballgame import FootballGame
from runrunlib.footballteam import FootballTeam


class FootballSimulationRunnerTests(TestCase):
    def test_should_pass_event(self):
        pass


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


if __name__ == '__main__':
    main()
