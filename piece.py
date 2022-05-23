from abc import abstractclassmethod


class Piece:
    color = "b"
    row = 0
    col = 0
    char = "X"

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

    @abstractclassmethod
    def move(self, board, row, col):
        raise NotImplementedError

    @abstractclassmethod
    def attack(self, board, row, col):
        raise NotImplementedError

    def print(
        self,
    ):
        print(self.char, end="")
