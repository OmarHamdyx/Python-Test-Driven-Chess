from model import Model


class View:
    def __init__(self):
        self.model = Model()

    def print_board(self):
        print(self.model.board)

    def showAlert(self):
        print("CHECKMATE!")

    def updateGameChat(self):
        print("In-game chat: ")
        for message in self.model.gameChat:
            print(message)
