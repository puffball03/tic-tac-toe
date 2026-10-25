import random
from abc import ABC, abstractmethod


class AIPlayer(ABC):
    """Base class for every computer opponent."""

    @abstractmethod
    def choose_move(self, board, mark):
        """Return a (row, col) tuple for an empty cell on the board."""


class MediumAI(AIPlayer):
    """Picks any empty cell at random."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        return self._rng.choice(board.empty_cells())


class HardAI(AIPlayer):
    """Uses Minimax algorithm to pick a cell"""

    def choose_move(self, board, mark):
        board = board.copy()
        opponent = "O" if mark == "X" else "X"
        best_score, best_move = float("-inf"), None
        for row, col in board.empty_cells():
            board.place_mark(row, col, mark)
            score = self._minimax(board, mark, opponent, False, 1)
            board.remove_mark(row, col)
            if score > best_score:
                best_score, best_move = score, (row, col)
        return best_move
    
    def _minimax(self, board, mark, opponent, is_maximizing, depth):
        if board.has_won(mark):
            return 10 - depth
        if board.has_won(opponent):
            return depth - 10
        if board.is_full():
            return 0
        
        current = mark if is_maximizing else opponent
        scores = []
        for row, col in board.empty_cells():
            board.place_mark(row, col, current)
            scores.append(self._minimax(board, mark, opponent, not is_maximizing, depth + 1))
            board.remove_mark(row, col)
        return max(scores) if is_maximizing else min(scores)
        


class EasyAI(AIPlayer):
    """Always picks the first empty cell. Predictable, so it is handy for testing."""

    def choose_move(self, board, mark):
        return board.empty_cells()[0]