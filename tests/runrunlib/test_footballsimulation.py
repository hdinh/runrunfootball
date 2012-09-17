from unittest import TestCase, skip, main
from runrunlib.footballsimulation import FootballSimulationGame
from runrunlib.footballgame import FootballGame
from runrunlib.footballteam import FootballTeam
from runrunlib.footballsimulation import football_simulation


class FootballSimulationRunnerTests(TestCase):
    def test_should_pass_clients_to_run_game(self):
        # Arrang & Act
        football_simulation.run_game(team1=FootballTeam('team1'),
                                     team2=FootballTeam('team2'),
                                     clients=())


class FootballSimulationGameTests(TestCase):
    def test_should_notify_events_to_clients(self):
        # Arrange
        teama = FootballTeam('team1')
        teamb = FootballTeam('team2')
        clients = ()

        simulation = FootballSimulationGame(team1=teama,
                                            team2=teamb,
                                            clients=clients)
        
        # Act
        game_result = simulation.sim_game()

        # Assert


if __name__ == '__main__':
    main()
