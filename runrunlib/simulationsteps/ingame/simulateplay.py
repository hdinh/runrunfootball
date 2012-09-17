from runrunlib.event import Event
from .a1simalgorithm import sim as a1sim

def simulate_football_play(state):
    return simulate_using_sim1_algorithm(state)

def simulate_using_sim1_algorithm(state):
    return a1sim(state)
