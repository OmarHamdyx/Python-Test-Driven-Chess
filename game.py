from view import View
from model import Model
from controller import Controller



def update_player(player):
    player.add_win()


def startGame(player):
    controller = Controller()
    model = Model()
    view = View()
    view.model = model
    controller.view = view
    controller.model = model
    controller.player = player
    is_game_over = False

    mode = input("Choose Game Mode: \n1 min [1]\n3 min[2]\n10 min[3]\n")
    type = input("Play Against Random[1]\nPlay Against Friend[2]\nPlay Against Computer[3]\n")
    controller.newGame()
    view.print_board()
    while 1:
        view.updateGameChat()
        move = input("Make your move\nTo type in chat, begin message with @\n")
        if move[0] == "@":
            controller.typeInChat(move)
            continue
        else:
            is_game_over = controller.makeMove(move)
            view.print_board()
        if is_game_over:
            view.showAlert()
            update_player(player)
            break

# fool's move: f3 , e5, g4, Qxh4,
