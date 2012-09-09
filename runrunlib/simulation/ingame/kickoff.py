from runrunlib.event import Event


def kickoff(state):
    if state.get_quarter() == 1 and \
       state.get_time() == 0:
        possession = state.get_possession()
        """
        possession = state.get_possession()
        decision1 = possession.decide(state)
        decision2 = state.get_other(possession).decide(state)
        _internal_simulate_game_action(state, decision1, decision2)
        """
        return state.event(KickOffEvent(possession.get_name() + ' kicked off'))
    else:
        return state


class KickOffEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)
