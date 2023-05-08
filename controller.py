from view import View
from model import Model
from player import Player


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.player = Player()

    def newGame(self):
        return self.model.initBoard()

    def typeInChat(self, message):
        self.model.gameChat.append(message)

    def surrender(self):
        self.player.losses += 1

    def makeMove(self,move):
        self.model.board.push_san(move)
        return self.model.isGameOver()
