from unittest import TestCase, main
from runrunlib.footballsimulationgamestate import FootballSimulationGameState
from runrunlib import footballrules, KickOffPlay, NormalPlay, KickOffPlayOutcome, NormalPlayOutcome
from runrunlib.footballteam import FootballTeam


class FootballRulesTests(TestCase):
    def test_get_play_type_should_be_kickoff_at_time0_quarter1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(1) \
                    .time(0)

        # Act & Assert
        self.assertEqual(footballrules.get_play_type(state), KickOffPlay)

    def test_get_play_type_should_be_kickoff_at_time0_quarter3(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(3) \
                    .time(0)

        # Act & Assert
        self.assertEqual(footballrules.get_play_type(state), KickOffPlay)

    def test_get_play_type_should_be_kickoff_at_time0_quarter5(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(5) \
                    .time(0)

        # Act & Assert
        self.assertEqual(footballrules.get_play_type(state), KickOffPlay)

    def test_get_play_type_should_not_be_kickoff_at_time0_quarter3_if_already_kicked_off(self):
        # Arrange
        teama = FootballTeam('teama')
        teamb = FootballTeam('teamb')
        state = FootballSimulationGameState() \
                    .team1(teama) \
                    .team2(teamb) \
                    .time(0)

        # Act & Assert
        self.assertNotEqual(KickOffPlay,
                            footballrules.get_play_type(state.quarter(3) \
                                                             .event(KickOffPlayOutcome(quarter=3,
                                                                                       time=0,
                                                                                       possession=teama,
                                                                                       nonpossession=teamb))))
        self.assertNotEqual(KickOffPlay,
                            footballrules.get_play_type(state.quarter(3) \
                                                             .event(NormalPlayOutcome(quarter=3,
                                                                                      time=0,
                                                                                      possession=teama,
                                                                                      nonpossession=teamb))))
        self.assertEqual(KickOffPlay,
                         footballrules.get_play_type(state.quarter(3) \
                                                          .event(NormalPlayOutcome(quarter=1,
                                                                                   time=0,
                                                                                   possession=teama,
                                                                                   nonpossession=teamb))))
 


    def test_get_play_type_should_not_be_kickoff_if_time_is_not_zero(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(1) \
                    .time(1)

        # Act & Assert
        self.assertNotEqual(footballrules.get_play_type(state), KickOffPlay)


if __name__ == '__main__':
    main()
