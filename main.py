from pawn import Pawn
from board import Board

if __name__ == "__main__":

    board = Board()
    board.print()

    pawn = board.board[6][0]
    pawn.move(board.board, 3, 0)
    board.print()
