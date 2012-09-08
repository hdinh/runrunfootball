from random import random

def process_state(state):
    pass

def _coin_flip(state):
    if state.get_time() == 0:
        if random() >= 0.5:
            winner = team1
        else:
            winner = team2
        return state.possession(coin_flip_winner)

_process_chain = [_coin_flip]
