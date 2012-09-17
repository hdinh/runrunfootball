from .teamcontroller import not_set_controller, default_controller_method
from .playbook import default_playbook


class _FootballTeamBase(object):
    def __init__(self,
                 name,
                 playbook):
        self._name = name
        self._playbook = playbook

    def get_name(self):
        return self._name

    def get_playbook(self):
        return self._playbook


class FootballTeam(_FootballTeamBase):
    def __init__(self,
                 name='NotNamed',
                 controller=None,
                 playbook=default_playbook):
        _FootballTeamBase.__init__(self, name, playbook)

        if controller == None:
            controller = default_controller_method()
        self._controller = controller

    def name(self, name):
        return FootballTeam(name=name,
                            controller=self._controller,
                            playbook=self._playbook)

    def controller(self, controller):
        return FootballTeam(name=self._name,
                            controller=controller,
                            playbook=self._playbook)

    def playbook(self, playbook):
        return FootballTeam(name=self._name,
                            controller=self._controller,
                            playbook=playbook)

    def get_controller(self):
        return self._controller

    def get_view_only_team(self):
        return ViewOnlyFootballTeam(self._name, self._playbook)

    def is_set(self):
        return True


class ViewOnlyFootballTeam(_FootballTeamBase):
    def __init__(self, name, playbook):
        _FootballTeamBase.__init__(self, name, playbook)


class NotSetTeam(object):
    def __init__(self):
        pass

    def get_name(self):
        return 'NotSet'

    def is_set(object):
        return False


not_set_team = NotSetTeam()
