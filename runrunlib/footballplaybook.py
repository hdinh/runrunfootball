class FootballPlaybook(object):
    def __init__(self,
                 name='Unnamed Playbook',
                 offense_plays=(),
                 defense_plays=()):
        self._name = name
        self._offense_plays = offense_plays
        self._defense_plays = defense_plays

    def name(self, name):
        return FootballPlaybook(name=name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays)

    def add_offense_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays + (play,),
                                defense_plays=self._defense_plays)

    def add_defense_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays + (play,))

    def remove_offense_play(self, play):
        temp = tuple(p for p in self._offense_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=temp,
                                defense_plays=self._defense_plays)

    def remove_defense_play(self, play):
        temp = tuple(p for p in self._defense_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=temp)

    def get_name(self):
        return self._name

    def get_offense_plays(self):
        return self._offense_plays

    def get_defense_plays(self):
        return self._defense_plays


default_playbook = FootballPlaybook()
