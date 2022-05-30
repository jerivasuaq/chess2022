from pawn import Pawn
from board import Board

if __name__ == "__main__":

    board = Board()
    board.print()

    #print('\n',"original board",'\n')
    
    pawn = board.board[6][3]
    pawn.move(board.board, 5, 3)
    board.print()

    #print('\n',"Mov peon",'\n')
    
    '''
    Testing king movements...

    b_king = board.board[7][3]
    b_king.move(board.board,6,4)
    board.print()
    print('\n',"Mov Rey",'\n')

    w_pawn = board.board[6][4]
    w_pawn.color='w'
    print('\n',"cambio color",'\n')
    b_king = board.board[7][3]
    b_king.move(board.board,6,4)
    board.print()
    print('\n',"Mov Rey",'\n')
    '''
