from . import KickOffReceivingPlay, \
              KickOffKickingPlay, \
              OffensePlay, \
              DefensePlay


class FootballTeamController(object):
    def __init__(self):
        pass


class CpuFootballTeamController(FootballTeamController):
    def choose_play(self, play_type, state, playbook):
        if play_type == KickOffReceivingPlay:
            return playbook.get_kickoff_receiving_plays()[0]
        elif play_type == KickOffKickingPlay:
            return playbook.get_kickoff_kicking_plays()[0]
        elif play_type == OffensePlay:
            return playbook.get_offense_plays()[0]
        elif play_type == DefensePlay:
            return playbook.get_defense_plays()[0]

    def is_set(object):
        return True


class NotSetController(FootballTeamController):
    def __init__(self):
        FootballTeamController.__init__(self)

    def is_set(object):
        return False


not_set_controller = NotSetController()
default_controller_method = CpuFootballTeamController
