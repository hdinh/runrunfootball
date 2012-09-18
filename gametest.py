from runrunlib.game import FootballGame
from runrunlib.team import FootballTeam
from runrunlib.gameclient import FootballGameClient


class ConsoleClient(FootballGameClient):
    def __init__(self):
        FootballGameClient.__init__(self)

    def on_event(self, event):
        print(event.get_description())


def main():
    console = ConsoleClient()

    teama = FootballTeam() \
                .name('teama')
    teamb = FootballTeam().name('teamb')

    game = FootballGame() \
            .gameid(1) \
            .team1(teama) \
            .team2(teamb) \
            .add_client(console)

    game.run()


if __name__ == '__main__':
    main()
