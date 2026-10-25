import pytest
import random
from ai import AIPlayer, EasyAI, HardAI

from board import Board

def test_abstract_cant_be_created():
    with pytest.raises(TypeError):
        ai = AIPlayer()

def test_easy_returns_empty():
    ai = EasyAI(rng=random.seed(42))
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(1, 1, "O")
    board.place_mark(0, 2, "O")
    assert ai.choose_move(board, "X") in board.empty_cells()

def test_hard_takes_winning_move():
    ai = HardAI()
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(1, 1, "O")
    assert ai.choose_move(board, "O") == (2, 2)

def test_choose_move_doesnt_fill_space_hard():
    ai = HardAI()
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(1, 1, "O")
    before = str(board)
    ai.choose_move(board, "O")
    assert before == str(board)
def test_choose_move_doesnt_fill_space_easy():
    ai = EasyAI()
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(1, 1, "O")
    before = str(board)
    ai.choose_move(board, "O")
    assert before == str(board)

