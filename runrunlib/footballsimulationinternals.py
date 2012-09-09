from random import random

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
        return state.possession(winner)

    return state

_process_chain = [_game_banner, _coin_flip]
