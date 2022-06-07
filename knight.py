from cmath import sqrt
from piece import Piece


class Knight(Piece):
    color = "b"
    char = "♞"
    def __init__(self, row, col) -> None:
        super().__init__(row, col)

    def _is_valid_move(self, board, row, col):
        if board[row][col] == None or board[row][col].color =='w':
            if self.color == "b":
                if (sqrt((self.row - row)**2 + (self.col-col)**2) == sqrt(10)):
                    return True
            elif self.color == "w":
                if (sqrt((self.row - row)**2 + (self.col-col)**2) == sqrt(10)):
                    return True
        print("Invalid movement")

    def move(self, board, row, col):
        if self._is_valid_move(board, row, col):
            board[row][col] = self
            board[self.row][self.col] = None

            self.row = row
            self.col = col

    def attack(self, board, row, col):
        pass