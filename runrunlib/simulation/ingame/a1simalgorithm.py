from . import FootballPlayOutcomeEvent

def sim(state):
    """
    play1 = state.get_possession().get_controller().choose_play()
    play2 = state.get_nonpossession().get_controller().choose_play()

    expected_gain = get_expected_gain()
    play_choose_points, t1 = compute_play_choose()
    offensive_quality_points, t2 = compute_offensive_quality()
    offensive_luck_points, t3 = compute_luck_points()
    """

    outcome = do_mix(state)
    return state.event(outcome)

def do_mix(state):
    return FootballPlayOutcomeEvent('')
