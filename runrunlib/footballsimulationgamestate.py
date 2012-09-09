from .footballteam import not_set_team

DEFAULT_QUARTER_COUNT = 4
DEFAULT_QUARTER_TIME = 60*15

class _FootballSimulationGameStateBase(object):
    def __init__(self,
                 gameid,
                 quarter_count,
                 quarter_time,
                 team1,
                 team2,
                 possession,
                 time,
                 quarter,
                 events):
        self._gameid = gameid
        self._quarter_count = quarter_count
        self._quarter_time = quarter_time
        self._team1 = team1
        self._team2 = team2
        self._possession = possession
        self._time = time
        self._quarter = quarter
        self._events = events

    def get_gameid(self):
        return self._gameid

    def get_quarter_count(self):
        return self._quarter_count

    def get_quarter_time(self):
        return self._quarter_time

    def get_team1(self):
        return self._team1

    def get_team2(self):
        return self._team2

    def get_possession(self):
        return self._possession

    def get_nonpossession(self):
        return self._team1 if self._possession == self._team2 else self._team2

    def get_time(self):
        return self._time

    def get_quarter(self):
        return self._quarter

    def get_events(self):
        return self._events


class FootballSimulationGameState(_FootballSimulationGameStateBase):
    def __init__(self,
                 gameid=-1,
                 quarter_count=DEFAULT_QUARTER_COUNT,
                 quarter_time=DEFAULT_QUARTER_TIME,
                 team1=not_set_team,
                 team2=not_set_team,
                 possession=not_set_team,
                 time=0,
                 quarter=1,
                 events=()):
        _FootballSimulationGameStateBase.__init__(self,
                                                  gameid,
                                                  quarter_count,
                                                  quarter_time,
                                                  team1,
                                                  team2,
                                                  possession,
                                                  time,
                                                  quarter,
                                                  events)

    def gameid(self, gameid):
        if self._gameid != -1:
            raise RuntimeError('gameid already set')

        return FootballSimulationGameState(gameid=gameid,
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def quarter_count(self, quarter_count):
        return FootballSimulationGameState(gameid=self._gameid,
                                           quarter_count=quarter_count,
                                           quarter_time=self._quarter_time,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def quarter_time(self, quarter_time):
        return FootballSimulationGameState(gameid=self._gameid,
                                           quarter_count=self._quarter_count,
                                           quarter_time=quarter_time,
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
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
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
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
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
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=team,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events)

    def time(self, time):
        return FootballSimulationGameState(gameid=self._gameid,
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
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
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=quarter,
                                           events=self._events)

    def event(self, event):
        return FootballSimulationGameState(gameid=self._gameid,
                                           quarter_count=self._quarter_count,
                                           quarter_time=self._quarter_time,
                                           team1=self._team1,
                                           team2=self._team2,
                                           possession=self._possession,
                                           time=self._time,
                                           quarter=self._quarter,
                                           events=self._events + (event,))

    def get_view_only_state(self):
        return ViewOnlyFootballSimulationGameState(gameid=self._gameid,
                                                   quarter_count=self._quarter_count,
                                                   quarter_time=self._quarter_time,
                                                   team1=self._team1.get_view_only_team(),
                                                   team2=self._team2.get_view_only_team(),
                                                   possession=self._possession.get_view_only_team(),
                                                   time=self._time,
                                                   quarter=self._quarter,
                                                   events=self._events)


class ViewOnlyFootballSimulationGameState(_FootballSimulationGameStateBase):
    def __init__(self,
                 gameid,
                 quarter_count,
                 quarter_time,
                 team1,
                 team2,
                 possession,
                 time,
                 quarter,
                 events):
        _FootballSimulationGameStateBase.__init__(self,
                                                  gameid,
                                                  quarter_count,
                                                  quarter_time,
                                                  team1,
                                                  team2,
                                                  possession,
                                                  time,
                                                  quarter,
                                                  events)
