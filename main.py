import pygame
import time
import sys
from pieces import Piece, Empty_Sqr

# Board list and size
board_x_max = 8
board_y_max = 8

# ## Create instances of all the pieces
# # Pawn, King, Queen, Bishop, Horse, Rook
def create_board(board):    
    # White pieces
    # board[0][0] = Piece('w', 'r', 'w_rook.png')
    # board[0][1] = Piece('w', 'h', 'w_horse.png')
    # board[0][2] = Piece('w', 'b', 'w_bishop.png')
    # board[0][3] = Piece('w', 'k', 'w_king.png')
    board[4][4] = Piece('w', 'q', 'w_queen.png')
    # board[0][5] = Piece('w', 'b', 'w_bishop.png')
    # board[0][6] = Piece('w', 'h', 'w_horse.png')
    # board[0][7] = Piece('w', 'r', 'w_rook.png')
    # White pawns
    # for i in range(board_x_max):
    #     board[1][i] = Piece('w', 'p', 'w_pawn.png')
        
    
    # Black pieces
    # board[7][0] = Piece('b', 'r', 'b_rook.png')
    # board[7][1] = Piece('b', 'h', 'b_horse.png')
    # board[4][2] = Piece('b', 'b', 'b_bishop.png')
    # board[7][3] = Piece('b', 'k', 'b_king.png')
    # board[7][4] = Piece('b', 'q', 'b_queen.png')
    # board[4][5] = Piece('b', 'b', 'b_bishop.png')
    # board[7][6] = Piece('b', 'h', 'b_horse.png')
    # board[7][7] = Piece('b', 'r', 'b_rook.png')
    # Black pawns
    for i in range(board_x_max):
        board[7][i] = Piece('b', 'p', 'b_pawn.png')
        
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

# breadth first search algorithm for movements
def BFS(pos, graph, board):
    pos = tuple(pos)
    visited = []
    visited.append(pos)
    queue = []
    queue.append(pos)
    
    while queue:
        m = queue.pop(0)
        
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                if(on_board(neighbour)):
                    test1 = board[neighbour[0]][neighbour[1]].team
                    test2 = board[pos[0]][pos[1]].team
                    if(board[neighbour[0]][neighbour[1]].team != board[pos[0]][pos[1]].team):
                        board[neighbour[0]][neighbour[1]].killable = True                        
                    else:
                        board[neighbour[0]][neighbour[1]].killable = False
                    if(board[neighbour[0]][neighbour[1]].team != None) and ((neighbour[0],neighbour[1]) in graph):
                            graph.pop(neighbour)
                            queue.pop(queue.index(neighbour))

    return board

# returns board pieces and movements
def pawn_moves():
    # TODO: determine graph input for BFS function
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

def queen_moves(pos, board):
    # TODO: determine graph input for BFS function and test with BFS function
    graph_dict = {}
    a = pos[1]-pos[0]
    b = pos[0]+pos[1]
    for y in range(board_y_max):
        graph_dict[(pos[0],y)] = []
        x = -y + b
        if(x >= 0 and x <= board_x_max-1):
            graph_dict[(x,y)] = []
    for x in range(board_x_max):
        if(x != pos[0]):
            graph_dict[(x,pos[1])] = []
        y = x + a
        if(y >= 0 and y <= board_y_max-1):
            if(y != pos[1]):        
                graph_dict[(x,y)] = []
    
    for y in range(board_y_max - pos[1]):
        if( (pos[0]+y+1,pos[1]+y+1) in graph_dict):
            graph_dict[(pos[0]+y,pos[1]+y)].append((pos[0]+y+1,pos[1]+y+1))
    for y in range(0,pos[1]-board_y_max,-1): # count with -1
        if( (pos[0]+y-1,pos[1]+y-1) in graph_dict):
            graph_dict[(pos[0]+y,pos[1]+y)].append((pos[0]+y-1,pos[1]+y-1))
    for x in range(board_x_max - pos[0]):
        if(x != pos[0]):
            if( (pos[0]+x+1,pos[1]-x-1) in graph_dict):
                graph_dict[(pos[0]+x,pos[1]-x)].append((pos[0]+x+1,pos[1]-x-1))
    for x in range(0,pos[0] - board_x_max,-1): # count with -1
        if(x != pos[0]):
            if( (pos[0]+x-1,pos[1]-x+1) in graph_dict):
                graph_dict[(pos[0]+x,pos[1]-x)].append((pos[0]+x-1,pos[1]-x+1))
    
    for y in range(board_y_max - pos[1]):
        if( (pos[0],pos[1]+y+1) in graph_dict):
            graph_dict[(pos[0],pos[1]+y)].append((pos[0],pos[1]+y+1))
    for y in range(0,pos[1]-board_y_max,-1):
        if( (pos[0],pos[1]+y-1) in graph_dict):
            graph_dict[(pos[0],pos[1]+y)].append((pos[0],pos[1]+y-1))
    for x in range(board_x_max - pos[0]):
        if(x != pos[0]):
            if( (pos[0]+x+1,pos[1]) in graph_dict):
                graph_dict[(pos[0]+x,pos[1])].append((pos[0]+x+1,pos[1]))
    for x in range(0,pos[0] - board_x_max,-1):
        if(x != pos[0]):
            if( (pos[0]+x-1,pos[1]) in graph_dict):
                graph_dict[(pos[0]+x,pos[1])].append((pos[0]+x-1,pos[1]))
                
    board = BFS(pos,graph_dict,board)
    
    return board

def bishop_moves(pos, board):
    # TODO: determine graph input for BFS function and test with BFS function
    graph_dict = {}
    a = pos[1]-pos[0]
    b = pos[0]+pos[1]
    for y in range(board_y_max):
        x = -y + b
        if(x >= 0 and x <= board_x_max-1):
            graph_dict[(x,y)] = []
    for x in range(board_x_max):
        y = x + a
        if(y >= 0 and y <= board_y_max-1):
            if(y != pos[1]):        
                graph_dict[(x,y)] = []
    
    for y in range(board_y_max - pos[1]):
        if( (pos[0]+y+1,pos[1]+y+1) in graph_dict):
            graph_dict[(pos[0]+y,pos[1]+y)].append((pos[0]+y+1,pos[1]+y+1))
    for y in range(0,pos[1]-board_y_max,-1): # count with -1
        if( (pos[0]+y-1,pos[1]+y-1) in graph_dict):
            graph_dict[(pos[0]+y,pos[1]+y)].append((pos[0]+y-1,pos[1]+y-1))
    for x in range(board_x_max - pos[0]):
        if(x != pos[0]):
            if( (pos[0]+x+1,pos[1]-x-1) in graph_dict):
                graph_dict[(pos[0]+x,pos[1]-x)].append((pos[0]+x+1,pos[1]-x-1))
    for x in range(0,pos[0] - board_x_max,-1): # count with -1
        if(x != pos[0]):
            if( (pos[0]+x-1,pos[1]-x+1) in graph_dict):
                graph_dict[(pos[0]+x,pos[1]-x)].append((pos[0]+x-1,pos[1]-x+1))
    
    board = BFS(pos,graph_dict,board)
    
    return board

def horse_moves(pos, board):
    # TODO: determine graph input for BFS function
    return 

def rook_moves(pos, board):
    # TODO: determine graph input for BFS function and test with BFS function
    graph_dict = {}
    for y in range(board_y_max):
        graph_dict[(pos[0],y)] = []
    for x in range(board_x_max):
        if(x != pos[0]):
            graph_dict[(x,pos[1])] = []
    
    for y in range(board_y_max - pos[1]):
        if( (pos[0],pos[1]+y+1) in graph_dict):
            graph_dict[(pos[0],pos[1]+y)].append((pos[0],pos[1]+y+1))
    for y in range(0,pos[1]-board_y_max,-1):
        if( (pos[0],pos[1]+y-1) in graph_dict):
            graph_dict[(pos[0],pos[1]+y)].append((pos[0],pos[1]+y-1))
    for x in range(board_x_max - pos[0]):
        if(x != pos[0]):
            if( (pos[0]+x+1,pos[1]) in graph_dict):
                graph_dict[(pos[0]+x,pos[1])].append((pos[0]+x+1,pos[1]))
    for x in range(0,pos[0] - board_x_max,-1):
        if(x != pos[0]):
            if( (pos[0]+x-1,pos[1]) in graph_dict):
                graph_dict[(pos[0]+x,pos[1])].append((pos[0]+x-1,pos[1]))
    
    board = BFS(pos,graph_dict,board)
    
    return board
    
 


def main():
    board = [[Empty_Sqr() for i in range(8)] for i in range(8)]
    board = create_board(board)
    # board = king_moves([0,3],board)
    # board = rook_moves([4,4],board)
    # board = bishop_moves([4,4],board)
    board = queen_moves([4,4],board)
    print(convert_to_readable(board))

if __name__ == '__main__':
    main()

    