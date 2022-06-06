from piece import Piece

class Rook(Piece):
    color = "b"
    char = "♜"

    def __init__(self, row, col) -> None:
        super().__init__(row, col)

    #Method to valiate if the piece movement is valid
    def _is_valid_move(self, board, row, col):

        dx, dy, blocked = 0, 0, 0

        #check if move is within board space
        if not(row < 0 or row > 7) and not(col < 0 or col > 7):
            #check the rook is moving into an empty space or one occupied by adversary piece
            if board[row][col] == None or board[row][col].color =='w':
                #check if rook is moving in its characteristic staight line t shape (forward, backward, sideways)
                dx = abs(self.row-row)
                dy = abs(self.col-col)
                if dx != 0 and dy == 0:
                    #check if another piece blocks the trayectory (rook cant jump)
                    blocked = 0
                    for i in range (self.col, col):
                        if board[row][i] != None:
                            blocked += 1
                    if blocked == 0:
                        return True
                    else:
                        print("Invalid movement")
                        return False
                elif dx == 0 and dy != 0:
                    #check if another piece blocks the trayectory (rook cant jump)
                    blocked = 0
                    for i in range (self.row, row):
                        if board[i][col] != None:
                            blocked += 1
                    if blocked == 0:
                        return True
                    else:
                        print("Invalid movement")
                        return False
                else:
                    print("Invalid movement")
                    return False
            else:
                print("Invalid movement")
                return False
        else:
            print("Invalid movement")
            return False

   #Attack method to eliminate the adversary piece object if required
    def attack(self, board, row, col):
        del board[row][col]

    def move(self, board, row, col):
        if self._is_valid_move(board, row, col):
            #attack(self, board, row, col)
            board[row][col] = self
            board[self.row][self.col] = None

            self.row = row
            self.col = col