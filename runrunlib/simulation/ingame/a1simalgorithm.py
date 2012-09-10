from runrunlib import footballrules

def sim(state):
    play_type = footballrules.get_play_type(state)

    """
    play1 = state.get_possession().get_controller().choose_play(play_type, state.get_view_only_state())
    play2 = state.get_nonpossession().get_controller().choose_play(play_type, state.get_view_only_state())

    expected_gain = get_expected_gain()
    play_choose_points, t1 = compute_play_choose()
    offensive_quality_points, t2 = compute_offensive_quality()
    offensive_luck_points, t3 = compute_luck_points()
    """

    #outcome = do_mix(state)
    #return state.event(outcome)
    from runrunlib import KickOffPlay, NormalPlay, KickOffPlayOutcome, NormalPlayOutcome
    if play_type == KickOffPlay:
        return state.event(KickOffPlayOutcome())
    else:
        return state.event(NormalPlayOutcome())

def do_mix(state):
    return NormalPlayOutcome('')
