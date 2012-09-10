from unittest import TestCase, main
from runrunlib.footballplaybook import FootballPlaybook


class FootballPlaybookTests(TestCase):
    def test_should_set_name(self):
        # Arrange & Act
        playbook = FootballPlaybook() \
                    .name('MyPlaybook')

        # Assert
        self.assertEqual(playbook.get_name(), 'MyPlaybook')

    def test_name_should_be_unamed_at_constructor(self):
        # Act & Assert
        self.assertEqual(FootballPlaybook().get_name(), 'Unnamed Playbook')


if __name__ == '__main__':
    main()
