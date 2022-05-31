from unittest import SkipTest
from board import Board
from king import King
from pawn import Pawn


def test_simple_test():
    assert True


def test_king_move_empty_space():
    board = Board(empty=True)
    b_king = King(3, 3)
    board.board[3][3] = b_king
    res = b_king.move(board.board, 3, 4)

    assert res is True


def test_king_move_not_valid_empty_space():
    board = Board(empty=True)
    b_king = King(3, 3)
    board.board[3][3] = b_king

    res = b_king.move(board.board, 1, 1)

    assert res is False


@SkipTest
def test_king_move_out_board():
    board = Board(empty=True)
    b_king = King(0, 0)
    board.board[0][0] = b_king

    res = b_king.move(board.board, 0, -1)

    assert res is False


@SkipTest  # TODO: create Rook class firest
def test_king_move_castling():
    board = Board(empty=True)

    b_king = King(7, 4)
    board.board[7][4] = b_king

    b_rook = Rook(7, 0)
    board.board[7][00] = b_rook

    res = b_king.move(board.board, 7, 2)
    assert res is True


def test_king_move_full_board_invalid_move_with_same_color_pawn():
    board = Board()
    b_king = King(7, 4)
    res = b_king.move(board.board, 6, 4)

    assert res is False


def test_king_atacks_white_pawn():
    board = Board(empty=True)

    b_king = King(7, 4)
    board.board[7][4] = b_king

    w_pawn = Pawn(6, 4)
    w_pawn.color = "w"
    board.board[6][4] = w_pawn

    res = b_king.move(board.board, 6, 4)

    assert res is True


def test_king_atacks_white_pawn():
    board = Board(empty=True)

    w_king = King(7, 4)
    w_king.color = "w"
    board.board[7][4] = w_king

    b_pawn = Pawn(6, 4)
    b_pawn.color = "b"
    board.board[6][4] = b_pawn

    res = w_king.move(board.board, 6, 4)

    assert res is True
