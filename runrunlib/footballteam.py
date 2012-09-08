class FootballTeam(object):
    def __init__(self, name='NotNamed'):
        self._name = name

    def name(self, name):
        return FootballTeam(name=name)

    def get_name(self):
        return self._name
