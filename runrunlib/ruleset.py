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


class FootballRuleset(object):
    def __init__(self,
                 quarter_count=4,
                 quarter_time=900):
        self._quarter_count = quarter_count
        self._quarter_time = quarter_time

    def quarter_count(self, quarter_count):
        return FootballRuleset(quarter_count=quarter_count,
                               quarter_time=self._quarter_time)

    def quarter_time(self, quarter_time):
        return FootballRuleset(quarter_count=self._quarter_count,
                               quarter_time=quarter_time)

    def get_quarter_count(self):
        return self._quarter_count

    def get_quarter_time(self):
        return self._quarter_time


default_ruleset = FootballRuleset()
