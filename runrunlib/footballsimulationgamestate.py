from .footballteam import not_set_team


class FootballSimulationGameState(object):
    def __init__(self,
                 gameid=-1,
                 team1=not_set_team,
                 team2=not_set_team,
                 possession=not_set_team,
                 time=0,
                 quarter=1,
                 events=()):
        self._gameid = gameid
        self._team1 = team1
        self._team2 = team2
        self._possession = possession
        self._time = time
        self._quarter = quarter
        self._events = events

    def gameid(self, gameid):
        if self._gameid != -1:
            raise RuntimeError('gameid already set')

        return FootballSimulationGameState(gameid=gameid,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def team1(self, team):
        if self._team1.is_set():
            raise RuntimeError('team1 already set')

        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=team,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def team2(self, team):
        if self._team2.is_set():
            raise RuntimeError('team2 already set')

        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=self._team1,
                                           team2=team,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def possession(self, team):
        if team not in [self._team1, self._team2]:
            raise RuntimeError('can only set possession to team1 or team2')
        
        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=team,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def time(self, time):
        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=time,
                                           quarter=self._quarter,
                                           events=self._events)

    def quarter(self, quarter):
        if quarter <= 0 or quarter >= 5:
            raise RuntimeError('quarter must be between 1 and 4')

        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=quarter,
                                           events=self._events)

    def event(self, event):
        return FootballSimulationGameState(gameid=self._gameid,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events + (event,))

    def get_gameid(self):
        return self._gameid

    def get_team1(self):
        return self._team1

    def get_team2(self):
        return self._team2

    def get_possession(self):
        return self._possession

    def get_time(self):
        return self._time

    def get_quarter(self):
        return self._quarter

    def get_events(self):
        return self._events
