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

while True:
    print(f"It is {game.turn}'s turn to move!")
    game.display_board()
    try:
        row = int(input("Enter the row number where you would like to place your mark"))
        col = int(input("Enter the column number where you would like to place your mark"))
    except:
        continue
    if game.play_move(row, col, game.turn):
        if game.has_won(game.turn):
            print(f"{game.turn} has won the game!")
            break
        game.switch_turns()
    else:
        print("You've typed an invalid move. Try again!")
        continue

    

