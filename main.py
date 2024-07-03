import pygame
import time
import sys
from pieces import Piece

# Board list and size
board_x_max = 8
board_y_max = 8

## Create instances of all the pieces
# Pawn, King, Queen, Bishop, Horse, Rook
# White pieces
wp = Piece('w', 'p', 'w_pawn.png')
wk = Piece('w', 'k', 'w_king.png')
wq = Piece('w', 'q', 'w_queen.png')
wb = Piece('w', 'b', 'w_bishop.png')
wh = Piece('w', 'h', 'w_horse.png')
wr = Piece('w', 'r', 'w_rook.png')

# Black pieces
bp = Piece('b', 'p', 'w_pawn.png')
bk = Piece('b', 'k', 'w_king.png')
bq = Piece('b', 'q', 'w_queen.png')
bb = Piece('b', 'b', 'w_bishop.png')
bh = Piece('b', 'h', 'w_horse.png')
br = Piece('b', 'r', 'w_rook.png')

def create_board(board):
    # White pieces
    board[0][0] = wr
    board[0][1] = wh
    board[0][2] = wb
    board[0][3] = wk
    board[0][4] = wq
    board[0][5] = wb
    board[0][6] = wh
    board[0][7] = wr
    # White pawns
    for i in range(board_x_max):
        board[1][i] = wp
    
    # Black pieces
    board[7][0] = br
    board[7][1] = bh
    board[7][2] = bb
    board[7][3] = bk
    board[7][4] = bq
    board[7][5] = bb
    board[7][6] = bh
    board[7][7] = br
    # Black pawns
    for i in range(board_x_max):
        board[6][i] = wp
        
    return board


## Create a readable format of the board
def convert_to_readable(board):
    output = ''
    
    for i in board:
        for j in i:
            try:
                output += j.team + j.type + '\t'
            except:
                output += j + '\t'
        output += '\n'
    return output

def possible_moves(piece, location):
    match piece:
        #Pawn
        case 'p':
            return pawn_moves()
        #King
        case 'k':
            return king_moves()
        #Queen
        case 'q':
            return queen_moves()
        #Bishop
        case 'b':
            return bishop_moves()
        #Horse
        case 'h':
            return horse_moves()
        #Rook
        case 'r':
            return rook_moves()
        #No piece
        case _:
            return None
            
            
# if move possible fill with 'o'
# if take possible fill with 'x'
# returns board pieces and movements

def pawn_moves():
    return 

def king_moves():
    return 

def queen_moves():
    return 

def bishop_moves():
    return

def horse_moves():
    return 

def rook_moves():
    return 
 


def main():
    board = [['  ' for i in range(8)] for i in range(8)]
    board = create_board(board)
    print(convert_to_readable(board))

if __name__ == '__main__':
    main()
    