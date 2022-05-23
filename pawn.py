from piece import Piece


class Pawn(Piece):
    color = "b"
    char = "♟️"

    def __init__(self, row, col) -> None:
        super().__init__(row, col)

    def _is_valid_move(self, board, row, col):
        if self.col == col:
            if self.color == "b":
                if (self.row - row) == 1:
                    return True
                if (self.row == 6) and (self.row - row == 2):
                    return True
            elif self.color == "w":
                if (self.row - row) == -1:
                    return True
                if (self.row == 1) and (self.row - row == -2):
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
