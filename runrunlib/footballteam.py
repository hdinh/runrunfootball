class FootballTeamController(object):
    def __init__(self):
        pass


class NotSetController(FootballTeamController):
    def __init__(self):
        FootballTeamController.__init__(self)

    def is_set(object):
        return False


not_set_controller = NotSetController()


class FootballTeam(object):
    def __init__(self,
                 name='NotNamed',
                 controller=not_set_controller):
        self._name = name
        self._controller = controller

    def name(self, name):
        return FootballTeam(name=name,
                            controller=self._controller)

    def controller(self, controller):
        return FootballTeam(name=self._name,
                            controller=controller)

    def get_name(self):
        return self._name

    def get_controller(self):
        return self._controller

    def is_set(self):
        return True


class NotSetTeam(object):
    def __init__(self):
        pass

    def get_name(self):
        return 'NotSet'

    def is_set(object):
        return False


not_set_team = NotSetTeam()
