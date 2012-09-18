from runrunlib.event import Event

from .quarterchanged import quarter_changed
from .quarterbanner import quarter_banner
from .simulateplay import simulate_football_play


def _default_pipeline():
    yield _stop_on(quarter_changed)
    yield _cont_on(quarter_banner)
    yield _stop_on(simulate_football_play)

def simulate_until_end(state):
    continue_until_end_predicate = lambda s: \
        s.get_quarter() < s.get_ruleset().get_quarter_count() and \
        s.get_time() < s.get_ruleset().get_quarter_time()

    return simulate_until(state, continue_until_end_predicate)

def simulate_until(state, continue_predicate, pipeline=_default_pipeline):
    while continue_predicate(state):
        state = simulate_once(state, pipeline)

    return state

def simulate_once(state, pipeline=_default_pipeline):
    for p in pipeline():
        state, should_stop = p(state)
        if should_stop:
            break

    return state

def _stop_on(f):
    def f_wrapped(state):
        state2 = f(state)
        should_continue = state2 != state
        return state2, should_continue
    return f_wrapped

def _cont_on(f):
    def f_wrapped(state):
        return f(state), False
    return f_wrapped
