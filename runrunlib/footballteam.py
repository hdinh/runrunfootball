from .footballteamcontroller import not_set_controller, default_controller_method


class _FootballTeamBase(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name


class FootballTeam(_FootballTeamBase):
    def __init__(self,
                 name='NotNamed',
                 controller=None):
        _FootballTeamBase.__init__(self, name)

        if controller == None:
            controller = default_controller_method()
        self._controller = controller

    def name(self, name):
        return FootballTeam(name=name,
                            controller=self._controller)

    def controller(self, controller):
        return FootballTeam(name=self._name,
                            controller=controller)

    def get_controller(self):
        return self._controller

    def get_view_only_team(self):
        return ViewOnlyFootballTeam(self._name)

    def is_set(self):
        return True


class ViewOnlyFootballTeam(_FootballTeamBase):
    def __init__(self, name):
        _FootballTeamBase.__init__(self, name)


class NotSetTeam(object):
    def __init__(self):
        pass

    def get_name(self):
        return 'NotSet'

    def is_set(object):
        return False


not_set_team = NotSetTeam()
