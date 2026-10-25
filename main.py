from board import Board
from game import Game

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
while True:
    mode = input("Type 1 for pvp mode, and 2 for vs AI")
    try: 
        mode = int(mode)
    except:
        print("Invalid Input Detected. Try again")
        continue
    if mode != 1 and mode != 2:
        print("Invalid Input Detected. Try again")    
    break
    
game = Game(player1, player2)

while True:
    print(f"\nIt is {game.turn}'s turn to move!")
    game.display_board()
    try:
        row, col = (int(x) - 1 for x in input("Enter the row(1-3), a space, then the column(1-3) where you would like to place your mark\nInput: ").split())
    except:
        print("You've typed an invalid move. Try again!\n")
        continue
    if game.play_move(row, col, game.turn):

        if game.has_won(game.turn):
            game.display_board()
            print(f"{game.turn} has won the game!")
            break
        if game.is_game_tied():
            game.display_board()
            print("Cats Game! No one wins...")
            break

        game.switch_turns()
    else:
        print("\nYou've typed an invalid move. Try again!")
        continue

    

