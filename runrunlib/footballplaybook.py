class FootballPlaybook(object):
    def __init__(self, name='Unnamed Playbook'):
        self._name = name

    def name(self, name):
        return FootballPlaybook(name=name)

    def get_name(self):
        return self._name


default_playbook = FootballPlaybook()
