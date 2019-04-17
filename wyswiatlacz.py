import string


plik = open('plik', 'r+')
board2 = plik.read().split('"')
plik.close()


board3 = split(str="],", num=board2.count(str))

def printBoard(board2):
    for row in board2:
        print(''.join(row))
    print()


printBoard(board2)
