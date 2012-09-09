from random import random
from .event import Event

import os


def process_state(state):
    for processor in _process_chain:
        state = processor(state)
    return state

def _game_start_banner(state):
    banner_lines = \
        ['=====================================',
         'Game ID  : %s' % state.get_gameid(),
         'Home team: %s' % state.get_team1().get_name(),
         'Away team: %s' % state.get_team2().get_name(),
         '=====================================']
    banner_string = os.linesep.join(banner_lines)
    return state.event(GameStartBannerEvent(banner_string))

def _coin_flip(state):
    if state.get_time() == 0 and not state.get_possession().is_set():
        if random() > 0.5:
            winner = state.get_team1()
        else:
            winner = state.get_team2()

        return state.event(CoinFlipEvent(winner.get_name() + ' won the coin flip')) \
                    .possession(winner)
    return state


class GameStartBannerEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)


class CoinFlipEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)

_process_chain = [_game_start_banner, _coin_flip]
