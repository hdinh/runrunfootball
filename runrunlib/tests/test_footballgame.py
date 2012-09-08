import unittest
from runrunlib import FootballGame, FootballTeam


class FootballGameTests(unittest.TestCase):
    @unittest.skip('need to do FooballTeam first')
    def test_should_be_named(self):
        team1 = FootballTeam()
        team2 = FootballTeam()
        game = FootballGame().name('TheGame').team1(team1).team2(team1)
