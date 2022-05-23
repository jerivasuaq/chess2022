from abc import abstractclassmethod, abstractmethod


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


class Pawn(Piece):
    color = "b"
    char = "♟️"

    def __init__(self, i, j) -> None:
        super().__init__(i, j)

    def move(i, j):
        pass

    def attack(i, j):
        pass


if __name__ == "__main__":
    s = [
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "pppppppp",
        "        ",
    ]
    board = [[None] * 8 for _ in range(8)]

    # filling the board
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] is not None:
                if s[i][j] == 'p':
                    p = Pawn(i, j)
                    board[i][j] = p


    # printing the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            p = board[i][j]
            if p is not None:
                p.print()
        print()
