from unittest import TestCase, main
from runrunlib.playfield import PlayField


class PlayFieldTests(TestCase):
    def test_should_define_playfield(self):
        # Arrange
        field = PlayField() \
                    .grid((100, 200))

        # Act
        x, y = field.get_grid()

        # Assert
        self.assertEqual(100, x)
        self.assertEqual(200, y)

    def test_get_yardline_should_return_yard_line_from_field_1(self):
        # Arrange
        field = PlayField().grid((200, 200))

        # Act & Assert
        self.assertEqual(0, field.get_yardline(0))
        self.assertEqual(10, field.get_yardline(20))
        self.assertEqual(50, field.get_yardline(100))
        self.assertEqual(70, field.get_yardline(140))
        self.assertEqual(95, field.get_yardline(190))

    def test_get_yardline_should_return_yard_line_from_field_2(self):
        # Arrange
        field = PlayField().grid((400, 300))

        # Act & Assert
        self.assertEqual(0, field.get_yardline(0))
        self.assertEqual(15, field.get_yardline(45))
        self.assertEqual(50, field.get_yardline(150))
        self.assertEqual(90, field.get_yardline(270))


if __name__ == '__main__':
    main()
