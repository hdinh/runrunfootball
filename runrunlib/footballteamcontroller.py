from . import KickOffPlay, NormalPlay


class FootballTeamController(object):
    def __init__(self):
        pass


class CpuFootballTeamController(FootballTeamController):
    def choose_play(self, play_type, state):
        if play_type == KickOffPlay:
            return KickOffPlay()
        elif play_type == NormalPlay:
            return NormalPlay()

    def is_set(object):
        return True


class NotSetController(FootballTeamController):
    def __init__(self):
        FootballTeamController.__init__(self)

    def is_set(object):
        return False


not_set_controller = NotSetController()
default_controller_method = CpuFootballTeamController
