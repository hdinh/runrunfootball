from runrunlib.event import Event


def simulate_until_end(state):
    continue_until_end_predicate = lambda s: \
        s.get_quarter() < s.get_quarter_count() and \
        s.get_time() < s.get_quarter_time()

    return simulate_until(state, continue_until_end_predicate)

def simulate_until(state, continue_predicate):
    while continue_predicate(state):
        state = simulate_once(state)

    return state

def simulate_once(state):
    for p in _pipeline:
        state, should_stop = p(state)
        if should_stop:
            break

    return state


class QuarterStartEvent(Event):
    def __init__(self, quarter):
        Event.__init__(self, 'Quarter ' + str(quarter) + ' has started')

def _stop_on(f):
    def f_wrapped(state):
        state2 = f(state)
        should_continue = state2 == state
        return state2, should_continue
    return f_wrapped

def _conintue_on(f):
    def f_wrapped(state):
        state2 = f(state)
        should_continue = state2 != state
        return state2, should_continue
    return f_wrapped



from .kickoff import kickoff
_pipeline = (_stop_on(kickoff,),)
             #continue_on(

simulate_to_end = simulate_until_end
