from player import Player
from random import randrange
import webbrowser
import game

players = []
forum_messages = []
leaderboard = []


def homepage(player):
    global leaderboard, players, forum_messages
    while 1:
        found = False
        choice = input(
            "Select Option\nStart Game[S]\nAdd Friend[A]\nOpen Forum[F]\nView Leaderboard[L]\nOpen Learning Section["
            "O]\nSign Out[SO]\n")
        if choice == "A":
            player_name = input("Enter Player Name: ")
            for i in range(0, len(players)):
                if player_name == players[i].name:
                    found = True
                    player.add_friend(players[i])
                    print("Player added successfully")
                    break
            if not found:
                print("Player not found")
        if choice == "F":
            print("Forum Posts: ")
            for i in range(0, len(forum_messages)):
                print(forum_messages[i])
            choice = input("Write a post[W]\nBack to Homepage[B]\n")
            if choice == "W":
                post = input("Write Here: \n")
                post = player.name + ": \n" + post
                forum_messages.append(post)
            elif choice == "B":
                continue
        if choice == "L":
            leaderboard = players.copy()
            leaderboard.sort(reverse=True)
            for i in range(0, len(leaderboard)):
                print(i + 1, ") ", leaderboard[i].name + ": level: ", leaderboard[i].level)
        if choice == "O":
            webbrowser.open('https://www.chess.com/learn-how-to-play-chess')
        if choice == "SO":
            break
        if choice == "S":
            game.startGame(player)


if __name__ == '__main__':
    print("Welcome to Chess Game")
    while 1:
        print("Log in to existing account [L]\nSign up a new account[S]\nSign in as a Guest[G]")
        choice = input()
        found = False
        if choice == "L":
            name = input("Enter your profile name: ")
            password = input("Enter your profile password: ")
            for i in range(0, len(players)):
                if name == players[i].name:
                    if password == players[i].password:
                        found = True
                        print("Welcome", name, "!")
                        homepage(players[i])
            if found == False:
                print("wrong credentials entered")
                continue

        elif choice == "S":
            new_player = Player()
            name = input("Enter your profile name: ")
            password = input("Enter your profile password: ")
            location = input("Enter your location: ")
            new_player.register(name, password, location)
            players.append(new_player)
            print("Welcome", name, "!")
            homepage(new_player)
        elif choice == "G":
            guest_name = "Guest" + str(randrange(0, 100))
            guest = Player()
            guest.name = guest_name
            print("Welcome", guest_name, "!")
            homepage(guest)
