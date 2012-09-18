from unittest import TestCase, main
from runrunlib.simulationgamestate import FootballSimulationGameState
from runrunlib import KickOffPlay, KickOffPlayOutcome
from runrunlib.team import FootballTeam
from runrunlib.ruleset import FootballRuleset
from runrunlib.simulationsteps.ingame.gameloop import simulate_once, \
                                                      simulate_until, \
                                                      simulate_until_end


class GameLoopTests(TestCase):
    def test_should_do_kickoff_at_quarter1_time0(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .time(0)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertTrue(KickOffPlayOutcome in map(lambda e: type(e), state2.get_events()))

    def test_should_not_do_kickoff_at_quarter1_time1(self):
        # Arrange
        state = FootballSimulationGameState() \
                    .team1(FootballTeam('teama')) \
                    .team2(FootballTeam('teamb')) \
                    .possession_index(0) \
                    .quarter(1) \
                    .time(1)

        # Act
        state2 = simulate_once(state)

        # Assert
        self.assertFalse(KickOffPlayOutcome in map(lambda e: type(e), state2.get_events()))

    def test_simulate_until_should_stop_and_return_state_once_predicate_is_false(self):
        # Arrange
        state = FootballSimulationGameState()

        class S: pass
        S.times = 0
        S.count = 0

        def once(state):
            S.times += 1
            return S.times == 1

        def countcalls(state):
            S.count += 1
            return state, True

        def mock_pipeline():
            yield countcalls

        # Act
        simulate_until(state, once, mock_pipeline)

        # Assert
        self.assertEqual(1, S.count)

    def test_simulate_until_end_should_run_until_quarter_and_time_expires(self):
        # Arrange
        ruleset = FootballRuleset() \
                    .quarter_count(2) \
                    .quarter_time(100)

        state = FootballSimulationGameState() \
                    .ruleset(ruleset)

        class S: pass
        S.count = 0

        def countcalls(state):
            S.count += 1
            if S.count >= 10:
                state = state.quarter(10)
            return state, True

        def mock_pipeline():
            yield countcalls

        # Act
        simulate_until_end(state, pipeline=mock_pipeline)

        # Assert
        self.assertEqual(10, S.count)


if __name__ == '__main__':
    main()
