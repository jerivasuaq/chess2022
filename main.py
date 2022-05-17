class Pawn:
    color = "b"
    i = 0
    j = 0

    def __init__(self, i, j) -> None:
        pass

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
    board = [[None] * 8] * 8

    # filling the board
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i][j] == "p":
                p = Peon(i, j)
                board[i][j] = p

    # printing the board
    for i in range(len(S)):
        for j in range(len(s)):
            p = board[i][j]
            if p:
                p.print()
