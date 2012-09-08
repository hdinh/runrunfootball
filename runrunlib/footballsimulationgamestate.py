class FootballSimulationGameState(object):
    def __init__(self, time=0):
        self._time = time

    def time(self, time):
        return FootballSimulationGameState(time=time)

    def get_time(self):
        return self._time
