from king import King
from pawn import Pawn


class Board:
    board = None

    def __init__(self) -> None:
        s = [
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "        ",
            "pppppppp",
            "   k    ",
        ]

        self.board = [[None] * 8 for _ in range(8)]

        # filling the board
        for row in range(len(s)):
            for col in range(len(s[0])):
                if s[row][col] is not None:
                    if s[row][col] == "p":
                        p = Pawn(row, col)
                        self.board[row][col] = p
                    if s[row][col] == "k":
                        p = King(row, col)
                        self.board[row][col] = p

    def print(self):
        # printing the board
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                p = self.board[row][col]
                if p is not None:
                    p.print()
                else:
                    print(" ", end="")
            print()
