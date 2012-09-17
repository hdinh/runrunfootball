from unittest import TestCase, main
from runrunlib.simulationsteps.pregame.pregamebanner import pregame_banner, \
                                                       GameStartBannerEvent
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib.team import FootballTeam


class PreGameBannerTests(TestCase):
    def test_should_add_game_start_event_banner_event(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb'))

        # Act
        state2 = pregame_banner(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], GameStartBannerEvent)


if __name__ == '__main__':
    main()
