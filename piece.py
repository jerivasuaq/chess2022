from abc import abstractclassmethod


class Piece:
    color = "b"
    i = 0
    j = 0
    char = "X"

    def __init__(self, i, j) -> None:
        self.i = i
        self.j = j

    @abstractclassmethod
    def move(self, i, j):
        raise NotImplementedError

    @abstractclassmethod
    def attack(self, i, j):
        raise NotImplementedError

    def print(
        self,
    ):
        print(self.char, end="")
