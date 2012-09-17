from runrunlib.event import Event
import os


def pregame_banner(state):
    banner_lines = \
        ['=====================================',
         'Game ID   : %s' % state.get_gameid(),
         'Home team : %s' % state.get_team1().get_name(),
         'Away team : %s' % state.get_team2().get_name(),
         '=====================================']
    banner_string = os.linesep.join(banner_lines)
    return state.event(GameStartBannerEvent(banner_string))


class GameStartBannerEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)
