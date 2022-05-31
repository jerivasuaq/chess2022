from ast import IsNot
from piece import Piece

class King(Piece):
    color = "b"
    char = "♚"

    def __init__(self, row, col) -> None:
        super().__init__(row, col)

    def _is_valid_move(self, board, row, col):
        if board[row][col] == None or board[row][col].color =='w':
            if self.color == "b":
                if abs((self.row - row)) <= 1 and abs((self.col-col))<=1:
                    return True
            elif self.color == "w":
                if (self.row - row) >= -1 and (self.col-col)>=-1:
                    return True

        return False

    def move(self, board, row, col):
        if self._is_valid_move(board, row, col):
            board[row][col] = self
            board[self.row][self.col] = None

            self.row = row
            self.col = col

            return True
        
        return False

    def attack(self, board, row, col):
        pass
