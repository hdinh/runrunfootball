from unittest import TestCase, main
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib import ruleset, KickOffPlay, NormalPlay, KickOffPlayOutcome, NormalPlayOutcome
from runrunlib.ruleset import default_ruleset, FootballRuleset
from runrunlib.team import FootballTeam


class FootballRulesetTests(TestCase):
    def test_get_play_type_should_be_kickoff_at_time0_quarter1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(1) \
                    .time(0)

        # Act & Assert
        self.assertEqual(ruleset.get_play_type(state), KickOffPlay)

    def test_get_play_type_should_be_kickoff_at_time0_quarter3(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(3) \
                    .time(0)

        # Act & Assert
        self.assertEqual(ruleset.get_play_type(state), KickOffPlay)

    def test_get_play_type_should_be_kickoff_at_time0_quarter5(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .quarter(5) \
                    .time(0)

        # Act & Assert
        self.assertEqual(ruleset.get_play_type(state), KickOffPlay)

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
                            ruleset.get_play_type(state.quarter(3) \
                                                       .event(KickOffPlayOutcome(quarter=3,
                                                                                 time=0,
                                                                                 possession=teama,
                                                                                 nonpossession=teamb))))
        self.assertNotEqual(KickOffPlay,
                            ruleset.get_play_type(state.quarter(3) \
                                                       .event(NormalPlayOutcome(quarter=3,
                                                                                time=0,
                                                                                possession=teama,
                                                                                nonpossession=teamb))))
        self.assertEqual(KickOffPlay,
                         ruleset.get_play_type(state.quarter(3) \
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
        self.assertNotEqual(ruleset.get_play_type(state), KickOffPlay)


class DefaultRuleset(TestCase):
    def test_get_quartercount_should_be_four(self):
        self.assertEqual(4, default_ruleset.get_quarter_count())

    def test_get_quartercount_should_be_four(self):
        self.assertEqual(900, default_ruleset.get_quarter_time())

    def test_should_set_quarter_count(self):
        # Arrange & Act
        state = FootballRuleset().quarter_count(3)

        # Assert
        self.assertEqual(state.get_quarter_count(), 3)

    def test_should_set_quarter_time(self):
        # Arrange & Act
        state = FootballRuleset().quarter_time(300)

        # Assert
        self.assertEqual(state.get_quarter_time(), 300)


if __name__ == '__main__':
    main()
