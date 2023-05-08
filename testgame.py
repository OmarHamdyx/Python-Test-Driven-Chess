import unittest
import chess
from controller import Controller


class TestGame(unittest.TestCase):

    def setUp(self):
        self.controller = Controller()

    def test_board(self):
        self.assertEqual(self.controller.newGame(), chess.Board())

    def test_type_in_game_chat(self):
        message = "testing"
        self.controller.typeInChat(message)
        self.assertIn(message, self.controller.model.gameChat)

    def test_surrender(self):
        self.controller.surrender()
        self.assertEqual(self.controller.player.losses, 1)

    def test_move_piece(self):
        self.controller.newGame()
        self.controller.makeMove("e4")
        self.assertNotEqual(self.controller.model.board, chess.Board())


if __name__ == '__main__':
    unittest.main()
