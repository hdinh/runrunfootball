from runrunlib.event import Event
from .a1simalgorithm import sim as a1sim

class FootballPlay(object):
    def execute(object, team_game_state):
        player0 = team_game_state.get_player(0)
        player0.get_rating('running.speed')

"""
_play_matrix = []
_play_matrix[0] = []
_play_matrix[1] = []
_play_matrix[2] = []
_play_matrix[3] = []
_play_matrix[4] = []
_play_matrix[5] = []
_play_matrix[6] = []
_play_matrix[7] = []
"""

def f(x1, x2, x3, x4, x5):
    state.get_team1().get_player()
    

def simulate_football_play(state):
    return simulate_using_sim1_algorithm(state)

def simulate_using_sim1_algorithm(state):
    return a1sim(state)
