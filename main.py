import pygame
import time
import sys
from pieces import Piece, Empty_Sqr

# Board list and size
board_x_max = 8
board_y_max = 8

# ## Create instances of all the pieces
# # Pawn, King, Queen, Bishop, Horse, Rook
# # White pieces
# wp = Piece('w', 'p', 'w_pawn.png')
# wk = Piece('w', 'k', 'w_king.png')
# wq = Piece('w', 'q', 'w_queen.png')
# wb = Piece('w', 'b', 'w_bishop.png')
# wh = Piece('w', 'h', 'w_horse.png')
# wr = Piece('w', 'r', 'w_rook.png')

# # Black pieces
# bp = Piece('b', 'p', 'b_pawn.png')
# bk = Piece('b', 'k', 'b_king.png')
# bq = Piece('b', 'q', 'b_queen.png')
# bb = Piece('b', 'b', 'b_bishop.png')
# bh = Piece('b', 'h', 'b_horse.png')
# br = Piece('b', 'r', 'b_rook.png')

# # Empty Sqr

def create_board(board):    
    # White pieces
    board[0][0] = Piece('w', 'r', 'w_rook.png')
    board[0][1] = Piece('w', 'h', 'w_horse.png')
    board[0][2] = Piece('w', 'b', 'w_bishop.png')
    board[0][3] = Piece('w', 'k', 'w_king.png')
    board[0][4] = Piece('w', 'q', 'w_queen.png')
    board[0][5] = Piece('w', 'b', 'w_bishop.png')
    board[0][6] = Piece('w', 'h', 'w_horse.png')
    board[0][7] = Piece('w', 'r', 'w_rook.png')
    # White pawns
    for i in range(board_x_max):
        board[1][i] = Piece('w', 'p', 'w_pawn.png')
        
    
    # Black pieces
    board[7][0] = Piece('b', 'r', 'b_rook.png')
    board[7][1] = Piece('b', 'h', 'b_horse.png')
    board[7][2] = Piece('b', 'b', 'b_bishop.png')
    board[7][3] = Piece('b', 'k', 'b_king.png')
    board[7][4] = Piece('b', 'q', 'b_queen.png')
    board[7][5] = Piece('b', 'b', 'b_bishop.png')
    board[7][6] = Piece('b', 'h', 'b_horse.png')
    board[7][7] = Piece('b', 'r', 'b_rook.png')
    # Black pawns
    for i in range(board_x_max):
        board[6][i] = Piece('b', 'p', 'b_pawn.png')
        
    return board


## Create a readable format of the board
# if move possible fill with 'o'
# if take possible fill with 'x'
def convert_to_readable(board):
    output = ''
    
    for i in board:
        for j in i:
            if(j.team != None):
                if(j.killable):
                    output += j.team + j.type + 'X' + '\t'
                else:
                    output += j.team + j.type + ' ' + '\t'
            elif(j.team == None):
                if(j.killable):
                    output += '  ' + 'O' + '\t'
                else:
                    output += '  ' + ' ' + '\t'
        output += '\n'
    return output

def possible_moves(piece, pos, board):
    match piece:
        #Pawn
        case 'p':
            return pawn_moves(pos, board)
        #King
        case 'k':
            return king_moves(pos, board)
        #Queen
        case 'q':
            return queen_moves(pos, board)
        #Bishop
        case 'b':
            return bishop_moves(pos, board)
        #Horse
        case 'h':
            return horse_moves(pos, board)
        #Rook
        case 'r':
            return rook_moves(pos, board)
        #No piece
        case _:
            return None


# check if on board [x,y]
def on_board(pos):
    #check for X spot
    if(pos[0] >= 0) and (pos[0] <= 7):
        if(pos[1] >= 0) and (pos[1] <= 7):
            return True
    return False


# returns board pieces and movements

def pawn_moves():
    return 

def king_moves(pos, board):
    for y in range(3):
        for x in range(3):
            if(on_board([pos[0] - 1 + x, pos[1] - 1 + y])):
                print(board[pos[0] - 1 + x][pos[1] - 1 + y].team)
                # if(board[pos[0] - 1 + x][pos[1] - 1 + y].team == None):
                #     board[pos[0] - 1 + x][pos[1] - 1 + y].killable = True
                # elif(board[pos[0] - 1 + x][pos[1] - 1 + y].team != board[pos[0]][pos[1]].team):                
                if(board[pos[0] - 1 + x][pos[1] - 1 + y].team != board[pos[0]][pos[1]].team): 
                    board[pos[0] - 1 + x][pos[1] - 1 + y].killable = True
                else:
                    board[pos[0] - 1 + x][pos[1] - 1 + y].killable = False                    
    return board

def queen_moves():
    return 

def bishop_moves():
    return

def horse_moves():
    return 

def rook_moves():
    return 
 


def main():
    board = [[Empty_Sqr() for i in range(8)] for i in range(8)]
    board = create_board(board)
    board = king_moves([0,3],board)
    print(convert_to_readable(board))

if __name__ == '__main__':
    main()
    