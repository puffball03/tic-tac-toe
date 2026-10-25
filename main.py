from board import Board
from game import Game
from random import randint

TITLE = r"""
       ____________________________________________________________
      /                                                           /
     /    _______         ______              ______             /
    /    /_  __(_)____   /_  __/___ ______   /_  __/___  ___    /
   /      / / / / ___/    / / / __ `/ ___/    / / / __ \/ _ \  /
  /      / / / / /__     / / / /_/ / /__     / / / /_/ /  __/ /
 /      /_/ /_/\___/    /_/  \__,_/\___/    /_/  \____/\___/ /
/___________________________________________________________/

                     X   /   O   /   X
                 -------/-------/-------
                   O   /   X   /   O
               -------/-------/-------
                 X   /   O   /   X

          >>>  P R E S S   E N T E R   T O   P L A Y  <<<
"""

_ = input(TITLE)
player1 = input("Type X or O to begin!\nInput: ")
player2 = "X" if player1 == "O" else "O"
game = Game(player1, player2)

turn = randint(0, 1)
while True:
    print(f"It is {player1 if turn == 0 else player2}'s turn to move!")
    game.display_board()
    try:
        row = int(input("Enter the row number where you would like to place your mark"))
        col = int(input("Enter the column number where you would like to place your mark"))
    except:
        continue
    if game.play_move(row, col, player1 if turn == 0 else player2):
        if turn == 0:
            turn = 1
        else:
            turn = 0
    else:
        print("You've typed an invalid move. Try again!")
    if turn == 1:
        if game.has_won(player1):
            print(f"{player1} has won the game!")
            break
    else:
        if game.has_won(player2):
            print(f"{player2} has won the game!")
            break


