class FootballGame(object):
    def __init__(self, gameid=-1):
        self._gameid = gameid

    def gameid(self, gameid):
        return FootballGame(gameid=gameid)

    def get_gameid(self):
        return self._gameid
