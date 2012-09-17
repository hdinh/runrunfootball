from unittest import TestCase, main
from runrunlib.simulationsteps.ingame.quarterbanner import quarter_banner, \
                                                           QuarterStartBannerEvent
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib.team import FootballTeam


class QuarterBannerTests(TestCase):
    def test_should_add_quarter_start_event_banner_at_time0(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(2) \
                    .time(0)

        # Act
        state2 = quarter_banner(state)

        # Assert
        self.assertIsInstance(state2.get_events()[-1], QuarterStartBannerEvent)

    def test_should_not_add_quarter_start_event_banner_at_time1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .quarter(2) \
                    .time(1)

        # Act
        state2 = quarter_banner(state)

        # Assert
        self.assertFalse(QuarterStartBannerEvent in map(lambda e: type(e), state2.get_events()))


if __name__ == '__main__':
    main()
