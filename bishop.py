from piece import Piece


class Bishop(Piece):
    color = "b"
    char = "♝"

    def __init__(self, row, col) -> None:
        super().__init__(row, col)

    def _is_valid_move(self, board, row, col):
        if (abs(self.row - row) == abs(self.col - col)):
            return True
        print("Invalid movement")

    def move(self, board, row, col):
        if self._is_valid_move(board, row, col):
            board[row][col] = self
            board[self.row][self.col] = None

            self.row = row
            self.col = col

    def attack(self, board, i, j):
        pass
