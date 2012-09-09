from random import random
from .event import Event

def process_state(state):
    for processor in _process_chain:
        state = processor(state)
    return state

def _game_banner(state):
    return state

def _coin_flip(state):
    if state.get_time() == 0 and not state.get_possession().is_set():
        if random() >= 0.5:
            winner = state.get_team1()
        else:
            winner = state.get_team2()

        return state.event(CoinFlipEvent(winner.get_name() + ' won the coin flip')) \
                    .possession(winner)

    return state

class CoinFlipEvent(Event):
    def __init__(self, description):
        Event.__init__(self, description)

_process_chain = [_game_banner, _coin_flip]
