from . import KickOffPlay, NormalPlay, FootballPlay, FootballPlayOutcome


def get_play_type(state):
    if state.get_time() == 0 and \
       state.get_quarter() in [1, 3, 5] and \
       not _play_exists(state.get_events(), state.get_quarter()):
        return KickOffPlay
    else:
        return NormalPlay

def _play_exists(events, quarter):
    # TODO: This is O(n) on the events, we can improve
    #       by storing the quarter as the key in hashmap
    for event in events:
        if issubclass(type(event), FootballPlayOutcome) and event.get_quarter() == quarter:
            return True
    return False
