from runrunlib.event import Event
import os


def quarter_banner(state):
    if state.get_time() == 0:
        banner_lines = \
            ['=====================================',
             'Quarter %s started' % str(state.get_quarter()),
             '=====================================']
        banner_string = os.linesep.join(banner_lines)
        return state.event(QuarterStartBannerEvent(banner_string))
    return state


class QuarterStartBannerEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)
