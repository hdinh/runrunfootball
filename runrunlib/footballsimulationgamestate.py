class FootballSimulationGameState(object):
    def __init__(self, time=0, quarter=1):
        self._time = time
        self._quarter = quarter

    def time(self, time):
        return FootballSimulationGameState(time=time,
                                           quarter=self._quarter)

    def quarter(self, quarter):
        if quarter <= 0 or quarter >= 5:
            raise RuntimeError('quarter must be between 1 and 4')
        return FootballSimulationGameState(time=self._time,
                                           quarter=quarter)

    def get_time(self):
        return self._time

    def get_quarter(self):
        return self._quarter
