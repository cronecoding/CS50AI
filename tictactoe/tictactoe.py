"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
    if x_count <= o_count:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range (3):
        for j in range (3):
            if board [i][j] is None:  #aka it is empty
                moves.add((i,j)) #add it as a possibility
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i not in range(3) or j not in range(3):
        raise ValueError("Action out of bounds")
    if board[i][j] is not EMPTY:
        raise ValueError("Cell is not empty")
    
    current = player(board)  #whose turn is it

    new_board = []  #create a copy board to explore with
    for row in board:
        new_row = []
        for cell in row:
            new_row.append(cell)
        new_board.append(new_row)

    new_board[i][j] = current   #try different moves

    return new_board #make a list of potential moves


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:  #three in a row
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY: #diagonals
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None #otherwise keep going


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    return True #no winner

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    the_winner = winner(board)

    if the_winner == "X":
        return 1
    if the_winner == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current = player(board)
    
    def max_value(board):
        if terminal(board):
            return utility(board)
        v = -float("inf")
        for action in actions(board):
            v = max(v, min_value(result(board,action)))
        return v
    
    def min_value(board):
        if terminal(board):
            return utility(board)
        v = float("inf")
        for action in actions(board):
            v = min(v,max_value(result(board,action)))
        return v
    
    if current == "X":
        best_score = -float("inf")
        best_move = None

        for action in actions(board):
            score = min_value(result(board, action))
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    
    else:
        best_score = float("inf")
        best_move = None

        for action in actions(board):
            score = max_value(result(board,action))
            if score < best_score:
                best_score = score
                best_move = action
        return best_move
    

