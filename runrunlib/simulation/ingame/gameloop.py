from runrunlib.event import Event


def simulate_until_end(state):
    return state


class QuarterStartEvent(Event):
    def __init__(self, quarter):
        Event.__init__(self, 'Quarter ' + str(quarter) + ' has started')

"""
def simulate_until_end(state):
    continue_game_predicate = lambda s: \
        return s.get_quarter() < s.get_num_quarters() and \
            s.get_time() < s.get_quarter_time()

    return simulate_until(state, continue_game_predicate)

def simulate_until(state, condition):
    while condition(state):
        state = _do_single_sim(state)

    return state

def _do_single_sim(state):
    for p in _pipeline:
        state, should_stop = p(state)
        if should_stop:
            break

    return state


from .kickoff import kickoff
_pipline = (kickoff,)

simulate_to_end = simulate_until_end
"""
