from unittest import TestCase, main
from runrunlib.game import FootballGame
from runrunlib.team import FootballTeam
#from runrunlib.footballgamerunner import FootballGameRunner


class FootballGameRunner(TestCase):
    def _test_playgrond(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')

        game = FootballGame() \
                .gameid(100) \
                .team1(teama) \
                .team2(teamb)

        console = ConsoleClient()

        runner = FootballGameRunner() \
                    .game(game) \
                    .add_client(console)

        # Act
        result = runner.run()

        # Assert


if __name__ == '__main__':
    main()
