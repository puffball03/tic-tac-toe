import pytest

from board import Board

def setup_board(positions, mark="X"):
    board = Board(3)
    for x, y in positions:
        board.place_mark(x, y, mark)
    return board

def test_legal_place_marker():
    """Tests that a valid marker placed on an empty space returns True"""
    board = Board(3)
    assert board.place_mark(1, 1, "O") == True

def test_illegal_mark_out_of_bounds():
    """Tests that an marker placed out of the range of the board returns False"""
    board = Board(3)
    assert board.place_mark(-1, 1, "O") == False

def test_illegal_mark_on_non_empty_space():
    board = Board(3)
    board.place_mark(1, 1, "O")
    assert board.place_mark(1, 1, "X") == False

def test_remove_mark_on_non_empty_space():
    board = Board(3)
    board.place_mark(1, 1, "O")
    board.remove_mark(1,1)
    assert board.is_empty(1,1) == True

def test_player_has_won_horizontal():
    board = setup_board([(1, 0),(1,1), (1,2)], mark="X")
    assert board.has_won("X") == True

def test_player_has_lost_horizontal():
    board = setup_board([(1, 0),(1,1), (1,2)], mark="X")
    assert board.has_won("O") == False

def test_player_has_won_vertical():
    board = setup_board([(0, 0),(1,0), (2,0)], mark="X")
    assert board.has_won("X") == True

def test_player_has_lost_vertical():
    board = setup_board([(0,0),(0,1),(0,2)], mark="X")
    assert board.has_won("O") == False

def test_player_has_won_diagonal_l2r():
    board = setup_board([(0,0),(1,1),(2,2)], mark="X")
    assert board.has_won("X") == True

def test_player_has_won_diagonal_r2l():
    board = setup_board([(0,2),(1,1),(2,0)], mark="X")
    assert board.has_won("X") == True

def test_if_board_is_full():
    board = setup_board([
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)], mark="X")
    assert board.is_full() == True

def test_if_board_is_not_full():
    board = setup_board([
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1)], mark="X")
    assert board.is_full() == False

def test_if_board_is_empty():
    board = Board(3)
    any_cell_has_a_tile = False
    for i in range(3):
        for j in range(3):
            if board.is_empty(i, j) == False:
                any_cell_has_a_tile = True
    assert any_cell_has_a_tile == False



