import random
from bot import move as m
def t3():
    board = createBoard()
    counter = 0
    marks = ['X', 'O']
    print(f'1|2|3\n4|5|6\n7|8|9')
    while True:
        if counter%2 == 0:
            userMove(board)
        if counter%2 == 1:
            botMove(board)
        if winCheck(board):
            return f'{marks[counter%2]} won the game!'
        counter += 1
   

def userMove(board):
    move = int(input('Enter a move: '))
    while not valid(move, board):
        move = int(input('Enter a valid move'))
    board[move] = 'X'
    print(boardPrint(board))

def botMove(board):
    move = m.botMove(board)
    print(move)
    board[move] = 'O'
    
    print(boardPrint(board))
    


def createBoard():
    return {1: '-', 2: '-', 3: '-', 4: '-', 5: '-', 6: '-', 7: '-', 8: '-', 9: '-'} 

def valid(move, board):
    if board[move] != '-':
        return False
    else:
        return True

def winCheck(board):
    if board[1] == board[2] == board[3] != '-':
        return True
    if board[4] == board[5] == board[6] != '-':
        return True
    if board[7] == board[8] == board[9] != '-':
        return True
    if board[1] == board[4] == board[7] != '-':
        return True
    if board[2] == board[5] == board[8] != '-':
        return True
    if board[3] == board[6] == board[9] != '-':
        return True
    if board[1] == board[5] == board[9] != '-':
        return True
    if board[3] == board[5] == board[7] != '-':
        return True

def boardPrint(board):
    return (f'{board[1]}|{board[2]}|{board[3]}\n{board[4]}|{board[5]}|{board[6]}\n{board[7]}|{board[8]}|{board[9]}')


def main():
    print(t3())


main()