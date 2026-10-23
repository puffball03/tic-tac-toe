class Game:
    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board
    
    #def create_game(self):
        
    def prompt_player(self) -> None:
        print("Input your Move")