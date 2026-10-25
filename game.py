from board import Board
from ai import EasyAI
class Game:
    def __init__(self, player1, player2, ai_player=None):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(3)
        self._turn = self.player1 if self.player1 == "X" else self.player2
        self.ai_player = ai_player

    def is_ai_turn(self):
        return self.ai_player is not None and self._turn == player2
    
    def play_ai_move(self):
        row, col = self.ai_player.choose_move(self.board, self._turn)
        return self.play_move(row, col, self._turn)
    
    def play_move(self, row, col, player):
        return self.board.place_mark(row, col, player)
    
    def switch_turns(self):
        if self._turn == self.player1:
            self._turn = self.player2
        else:
            self._turn = self.player1
    @property
    def turn(self):
        return self._turn

    def has_won(self, player):
        return self.board.has_won(player)

    def score(self):
        if board.has_won(self.player1):
            return 10
        elif board.has_won(self.player2):
            return -10
        else:
            return 0

    def display_board(self):
        #This is technically a print outside of the main.py, but it cleans up the main code.
        print(self.board)

    def is_game_over(self, player):
        return self.board.has_won(player)
    def is_game_tied(self):
        return self.board.is_full()