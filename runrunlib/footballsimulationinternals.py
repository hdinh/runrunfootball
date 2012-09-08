from random import random

def process_state(state):
    for processor in _process_chain:
        state = processor(state)
    return state

def _coin_flip(state):
    if state.get_time() == 0:
        if random() >= 0.5:
            winner = state.get_team1()
        else:
            winner = state.get_team2()
        return state.possession(winner)

    return state

_process_chain = [_coin_flip]
