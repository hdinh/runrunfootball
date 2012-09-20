from unittest import TestCase, main
from runrunlib import FootballPlay, \
                      KickOffKickingPlay, \
                      KickOffReceivingPlay, \
                      OffensePlay, \
                      DefensePlay


class FootballPlayContractTests(object):
    def test_should_set_name_and_return(self):
        # Act
        play = self.get_klass()() \
                .name('Fly Pattern')

        # Assert
        self.assertEqual('Fly Pattern', play.get_name())


class KickOffKickingPlayTests(TestCase, FootballPlayContractTests):
    def get_klass(self):
        return KickOffKickingPlay


class KickOffReceivingPlayTests(TestCase, FootballPlayContractTests):
    def get_klass(self):
        return KickOffReceivingPlay


class OffensePlayTests(TestCase, FootballPlayContractTests):
    def get_klass(self):
        return OffensePlay


class DefensePlayTests(TestCase, FootballPlayContractTests):
    def get_klass(self):
        return DefensePlay


if __name__ == '__main__':
    main()
