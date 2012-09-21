from runrunlib import ruleset, \
                      KickOffPlay, \
                      KickOffPlayOutcome, \
                      NormalPlayOutcome


def sim(state):
    play_type = ruleset.get_play_type(state)

    #import pdb; pdb.set_trace()
    play1 = state.get_possession() \
                 .get_controller() \
                 .choose_play(play_type,
                              state.get_view_only_state(),
                              state.get_possession().get_playbook())

    play2 = state.get_nonpossession() \
                 .get_controller() \
                 .choose_play(play_type,
                              state.get_view_only_state(),
                              state.get_nonpossession().get_playbook())

    #if play1.get_play_type() == PlayType.Run:
    #    return 5
    #elif play
    #expected_gain1 = play1.get_expected_gain()
    #z = compare_plays(play1, play2)
    #quality1 = get_quality(state.get_possession())
    #quality2 = get_quality(state.get_nonpossession())
    #offensive_quality_points, t2 = compute_offensive_quality()
    #offensive_luck_points, t3 = compute_luck_points()

    #outcome = do_mix(state)
    #return state.event(outcome)
    from runrunlib import KickOffPlay, NormalPlay, KickOffPlayOutcome, NormalPlayOutcome
    if play_type == KickOffPlay:
        return state.event(KickOffPlayOutcome(state.get_quarter(),
                                              state.get_time(),
                                              state.get_possession(),
                                              state.get_nonpossession()))
    else:
        return state.event(NormalPlayOutcome(state.get_quarter(),
                                             state.get_time(),
                                             state.get_possession(),
                                             state.get_nonpossession()))


def do_mix(play1, play2):
    return NormalPlayOutcome('')
