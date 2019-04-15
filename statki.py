import random

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def generateBoard():
    board = getNewBoard()
    placeShips(board)
    return board


def printBoard(board):
    for row in board:
        print(''.join(row))
    print()


def getNewBoard():
    return [['0' for i in range(10)] for j in range(10)]


def placeShips(board):
    try:
        for ship in ships:
            placeShip(board, ship)
    except RecursionError:
        placeShips(board)


def placeShip(board, ship):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    direction = random.randint(0, 1)
    shipX = ship if direction == 0 else 0
    shipY = ship if direction == 1 else 0
    limits = [x - 1, x + shipX + 1, y - 1, y + shipY + 1]
    for i, limit in enumerate(limits):
        if limit < -1 or limit > 10:
            return placeShip(board, ship)
        if limit < 0:
            limits[i] = 0
        elif limit > 9:
            limits[i] = 9
    xMin = limits[0]
    xMax = limits[1]
    yMin = limits[2]
    yMax = limits[3]
    taken = False
    for i in range(xMax - xMin + 1):
        x1 = i + xMin
        for j in range(yMax - yMin + 1):
            y1 = j + yMin
            if board[y1][x1] == '1':
                taken = True
    if taken == True:
        return placeShip(board, ship)
    else:
        if direction == 0:
            for i in range(ship):
                board[y][i + x] = '1'
        else:
            for i in range(ship):
                board[i + y][x] = '1'


board = generateBoard()
printBoard(board)
