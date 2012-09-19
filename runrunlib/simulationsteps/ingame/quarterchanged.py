from runrunlib.event import Event


def quarter_changed(state):
    if state.get_time() >= state.get_ruleset().get_quarter_time():
        return state.quarter(state.get_quarter() + 1) \
                    .time(0) \
                    .event(QuarterChangedEvent(state.get_quarter(), state.get_quarter() + 1))
    return state


class QuarterChangedEvent(Event):
    def __init__(self, quarter_from, quarter_to):
        Event.__init__(self, 'changed quarter from %s to %s' % (quarter_from, quarter_to))
