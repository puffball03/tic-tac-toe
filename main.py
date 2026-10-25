from board import Board
from game import Game
from ai import EasyAI, HardAI

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

level = 0

def choose_opponents():
    while True:
        mode = input("Type 1 for pvp mode, and 2 for vs AI\nInput: ")
        if mode == "1":
            return None
        if mode == "2":
            level = input("Which difficulty level would you like to play against? (Easy/Hard)\nInput: ").strip().lower()
            if level == "hard":
                return HardAI()
            else:
                return EasyAI() 

game = Game("X", "O", ai_player = choose_opponents())

while True:
    print(f"\nIt is {game.turn}'s turn to move!")
    game.display_board()
    mark = game.turn
    if game.is_ai_turn():
        game.play_ai_move()
        print(f"\nAI {mark} moved")
    else:
        try:
            row, col = (int(x) - 1 for x in input("Enter the row(1-3), a space, then the column(1-3) where you would like to place your mark\nInput: ").split())
        except ValueError:
            print("You've typed an invalid move. Try again!\n")
            continue
        if not game.play_move(row, col, mark):
            print("Illegal move. Please try again.")
            continue

    if game.has_won(mark):
        game.display_board()
        print(f"{mark} has won the game!")
        break
    if game.is_game_tied():
        game.display_board()
        print("Cats Game! No one wins...")
        break

    game.switch_turns()



