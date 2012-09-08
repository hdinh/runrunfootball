from .footballgameresult import _FootballGameResult


class _FootballLogic(object):
    def run_game(self, team1, team2):
        return _FootballGameResult(team1)

football_logic = _FootballLogic()
