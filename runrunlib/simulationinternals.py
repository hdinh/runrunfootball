from .event import Event

import os
from random import random


def process_state(state):
    for processor in _process_chain:
        state = processor(state)
    return state

def _internal_simulate_game_action(state, decision1, decision2):
    # TODO
    pass

def _gameloop(state):
    # TODO
    pass

def _game_done_banner(state):
    # TODO
    pass


#_process_chain = (_game_start_banner, _coin_flip, _kickoff, _gameloop, _game_done_banner)
