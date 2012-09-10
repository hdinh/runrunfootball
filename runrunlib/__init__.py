from .event import Event


class FootballPlay(object):
    def __init__(self):
        pass


class KickOffPlay(FootballPlay):
    def __init__(self):
        FootballPlay.__init__(self)


class NormalPlay(FootballPlay):
    def __init__(self):
        FootballPlay.__init__(self)


class KickOffKickingPlay(KickOffPlay):
    def __init__(self):
        KickOffPlay.__init__(self)


class KickOffReceivingPlay(KickOffPlay):
    def __init__(self):
        KickOffPlay.__init__(self)


class OffensePlay(NormalPlay):
    def __init__(self):
        NormalPlay.__init__(self)


class DefensePlay(NormalPlay):
    def __init__(self):
        DefensePlay.__init__(self)


class FootballPlayOutcome(Event):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession,
                 description):
        Event.__init__(self, description)
        self._quarter = quarter
        self._time = time
        self._possession = possession
        self._nonpossession = nonpossession

    def get_quarter(self):
        return self._quarter

    def get_time(self):
        return self._time

    def get_possession(self):
        return self._possession

    def get_nonpossession(self):
        return self._nonpossession


class KickOffPlayOutcome(FootballPlayOutcome):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession,
                 description=''):
        FootballPlayOutcome.__init__(self,
                                     quarter,
                                     time,
                                     possession,
                                     nonpossession,
                                     description)


class NormalPlayOutcome(FootballPlayOutcome):
    def __init__(self,
                 quarter,
                 time,
                 possession,
                 nonpossession,
                 description=''):
        FootballPlayOutcome.__init__(self,
                                     quarter,
                                     time,
                                     possession,
                                     nonpossession,
                                     description)
