import json


plik = open('plik', 'r+')
board = json.loads(plik.read())
plik.close()


def printBoard(board):
    for row in board:
        print(''.join(row))
    print()


printBoard(board)
