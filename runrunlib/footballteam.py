class FootballTeam(object):
    def __init__(self, name='NotNamed'):
        self._name = name

    def name(self, name):
        return FootballTeam(name=name)

    def get_name(self):
        return self._name

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
