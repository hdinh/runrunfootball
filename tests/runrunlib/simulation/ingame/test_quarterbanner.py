from unittest import TestCase, main
from runrunlib.simulation.ingame.quarterbanner import quarter_banner, \
                                                      QuarterStartBannerEvent
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib.footballteam import FootballTeam


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


if __name__ == '__main__':
    main()
