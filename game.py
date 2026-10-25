from board import Board

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board(3)
        self._turn = 0
        self._game_over
    
    def play_move(self, row, col, player):
        board.place_mark(row, col, player)
        
    def prompt_player(self) -> None:
        print("Input your Move")