from board import Board
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(3)
        self._turn = player1 if randint(0,1) == 0 else player2
    
    def play_move(self, row, col, player):
        return self.board.place_mark(row, col, player)

    @property
    def turn(self):
        return self._turn

    def has_won(self, player):
        return self.board.has_won(player)

    def display_board(self):
        print(self.board)
    def is_game_over(self, player):
        return board.has_won(player)