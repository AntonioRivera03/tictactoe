import random

class move():

    def botMove(board):
        if 'O' != board[1] and 'O' != board[2] and 'O' != board[3] and 'O' != board[4] and 'O' != board[5] and 'O' != board[6] and 'O' != board[7] and 'O' != board[8] and 'O' != board[9]:
            print('O not in board')
            return move.firstMove(board)
        else:
            return move.pattern(board)

    def firstMove(board):
        if board[5] == '-':
            return 5
        if board[1] == '-':
            return 1
        if board[3] == '-':
            return 3
        if board[7] == '-':
            return 7
        if board[9] == '-':
            return 9


    def pattern(board):
    
        move = random.randint(1,9)
        while board[move] != '-':
            move = random.randint(1,9)
        return move