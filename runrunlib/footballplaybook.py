class FootballPlaybook(object):
    def __init__(self,
                 name='Unnamed Playbook',
                 offense_plays=(),
                 defense_plays=(),
                 kickoff_receiving_plays=(),
                 kickoff_kicking_plays=()):
        self._name = name
        self._offense_plays = offense_plays
        self._defense_plays = defense_plays
        self._kickoff_receiving_plays = kickoff_receiving_plays
        self._kickoff_kicking_plays = kickoff_kicking_plays

    def name(self, name):
        return FootballPlaybook(name=name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def add_offense_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays + (play,),
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def add_defense_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays + (play,),
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def add_kickoff_receiving_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays + (play,),
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def add_kickoff_kicking_play(self, play):
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays + (play,))


    def remove_offense_play(self, play):
        temp = tuple(p for p in self._offense_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=temp,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def remove_defense_play(self, play):
        temp = tuple(p for p in self._defense_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=temp,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def remove_kickoff_receiving_play(self, play):
        temp = tuple(p for p in self._kickoff_receiving_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=temp,
                                kickoff_kicking_plays=self._kickoff_kicking_plays)

    def remove_kickoff_kicking_play(self, play):
        temp = tuple(p for p in self._kickoff_kicking_plays if p != play)
        return FootballPlaybook(name=self._name,
                                offense_plays=self._offense_plays,
                                defense_plays=self._defense_plays,
                                kickoff_receiving_plays=self._kickoff_receiving_plays,
                                kickoff_kicking_plays=temp)

    def get_name(self):
        return self._name

    def get_offense_plays(self):
        return self._offense_plays

    def get_defense_plays(self):
        return self._defense_plays

    def get_kickoff_receiving_plays(self):
        return self._kickoff_receiving_plays

    def get_kickoff_kicking_plays(self):
        return self._kickoff_kicking_plays


default_playbook = FootballPlaybook()
