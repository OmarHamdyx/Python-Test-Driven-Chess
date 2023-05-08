import unittest
from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_register(self):
        name = input()
        password = input()
        location = input()
        self.player.register(name, password, location)
        self.assertEqual(self.player.name, name)
        self.assertEqual(self.player.password, password)
        self.assertEqual(self.player.location, location)

    def test_add_friend(self):
        friend = Player()
        friend.name = "hamdy"
        self.player.add_friend(friend)
        self.assertIn(friend, self.player.friends)

    def test_level(self):
        self.player.wins = 10
        self.player.losses = 5
        self.player.adjust_level()
        self.assertEqual(self.player.level, 2)


if __name__ == '__main__':
    unittest.main()
