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

def test_if_board_is_full_non_win():
    board = Board(3)
    board.place_mark(0, 0, "X")
    board.place_mark(1, 0, "O")
    board.place_mark(0, 1, "X")
    board.place_mark(0, 2, "O")
    board.place_mark(1, 2, "X")
    board.place_mark(1, 1, "O")
    board.place_mark(2, 0, "X")
    board.place_mark(2, 1, "O")
    board.place_mark(2, 2, "X")
    assert board.is_full() == True

def test_if_board_is_empty():
    board = Board(3)
    any_cell_has_a_tile = False
    for i in range(3):
        for j in range(3):
            if board.is_empty(i, j) == False:
                any_cell_has_a_tile = True
    assert any_cell_has_a_tile == False

@pytest.mark.parametrize("cell, position", [
    (1, (0, 0)),
    (2, (0, 1)),
    (3, (0, 2)),
    (4, (1, 0)),
    (5, (1, 1)),
    (6, (1, 2)),
    (7, (2, 0)),
    (8, (2, 1)),
    (9, (2, 2)),
])
def test_cell_to_position(cell, position):
    board = Board(3)
    assert board.cell_to_position(cell) == position

def test_cell_zero_is_illegal():
    board = Board(3)
    row, col = board.cell_to_position(0)
    assert board.place_mark(row, col, "X") == False

def test_cell_ten_is_illegal():
    board = Board(3)
    row, col = board.cell_to_position(10)
    assert board.place_mark(row, col, "X") == False

def test_cell_on_non_empty_space_is_illegal():
    board = Board(3)
    row, col = board.cell_to_position(5)
    board.place_mark(row, col, "O")
    assert board.place_mark(row, col, "X") == False

def test_example_board_shows_digits():
    board = Board(3)
    assert board.example() == (
        "1 | 2 | 3\n"
        "--+---+--\n"
        "4 | 5 | 6\n"
        "--+---+--\n"
        "7 | 8 | 9"
    )

def test_example_board_ignores_marks():
    board = Board(3)
    board.place_mark(1, 1, "X")
    before = str(board)
    assert "5" in board.example()
    assert before == str(board)



