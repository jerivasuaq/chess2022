from pawn import Pawn

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
                if s[i][j] == "p":
                    p = Pawn(i, j)
                    board[i][j] = p

    # printing the board
    for i in range(len(board)):
        for j in range(len(board[0])):
            p = board[i][j]
            if p is not None:
                p.print()
        print()
