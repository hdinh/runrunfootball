from unittest import TestCase, skip
from runrunlib.footballsimulationinternals import process_state
from runrunlib.footballsimulation import _FootballGameSimulationState


class FootballSimulationInteralsTest(TestCase):
    @skip('depends on simulation state')
    def test_prococess_state_should_do_coin_flip_if_initial(self):
        state = self._FootballGameSimulationState() \
                    .time(0) \
                    .quarter(0)
