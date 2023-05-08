import chess
class Model:
    def __init__(self):
        self.board=None
        self.gameChat=[]

    def initBoard(self):
        self.board = chess.Board()
        return self.board

    def isGameOver(self):
        return self.board.is_checkmate()

