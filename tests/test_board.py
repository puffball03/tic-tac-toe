from board import Board

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
