from .event import Event


DEFAULT_NAME = 'Not named'


class FootballPlay(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class KickOffPlay(FootballPlay):
    def __init__(self, name):
        FootballPlay.__init__(self, name)


class NormalPlay(FootballPlay):
    def __init__(self, name):
        FootballPlay.__init__(self, name)


class KickOffKickingPlay(KickOffPlay):
    def __init__(self, name=DEFAULT_NAME):
        KickOffPlay.__init__(self, name)

    def name(self, name):
        return KickOffKickingPlay(name=name)


class KickOffReceivingPlay(KickOffPlay):
    def __init__(self, name=DEFAULT_NAME):
        KickOffPlay.__init__(self, name)

    def name(self, name):
        return KickOffReceivingPlay(name=name)


class OffensePlay(NormalPlay):
    def __init__(self, name=DEFAULT_NAME):
        NormalPlay.__init__(self, name)

    def name(self, name):
        return OffensePlay(name=name)


class DefensePlay(NormalPlay):
    def __init__(self, name=DEFAULT_NAME):
        NormalPlay.__init__(self, name)

    def name(self, name):
        return DefensePlay(name=name)


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
