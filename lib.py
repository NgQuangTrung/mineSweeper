import random
import param_var

def gameDataInit(size: set, minePos: list):
    tmp = [['-'] * size[1] for _ in range(size[0])]
    for y, x in minePos:
        tmp[y][x] = 'x'

    for y in range(size[0]):
        for x in range(size[1]):
            tmp[y][x] = bombCount((y, x), tmp, size)
    param_var.gameDataLayout = tmp


def mine_setup(size: set, no_of_mines: int):
    while len(param_var.minePos) < no_of_mines:
        tmp = (random.randint(0, size[1] - 1),
               random.randint(0, size[0] - 1))

        if tmp not in param_var.minePos:
            param_var.minePos.append(tmp)


def bombCount(pos: set, gameDataLayout: list, size: set):
    y, x = pos
    height, width = size
    n = 0

    if gameDataLayout[y][x] != 'x':
        if x == 0 and y == 0:
            n = n+1 if gameDataLayout[y][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x+1] == 'x' else n
        elif x == 0 and y == height:
            n = n+1 if gameDataLayout[y][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x+1] == 'x' else n
        elif x == 0 and y in range(1, height-1):
            n = n+1 if gameDataLayout[y-1][x] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x] == 'x' else n

        elif x == width and y == 0:
            n = n+1 if gameDataLayout[y][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x] == 'x' else n
        elif x == width and y == height:
            n = n+1 if gameDataLayout[y][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x] == 'x' else n
        elif x == width and y in range(1, height-1):
            n = n+1 if gameDataLayout[y-1][x] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x] == 'x' else n

        elif x in range(1, width-1) and y in range(1, height-1):
            n = n+1 if gameDataLayout[y-1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x] == 'x' else n
            n = n+1 if gameDataLayout[y-1][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y][x+1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x-1] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x] == 'x' else n
            n = n+1 if gameDataLayout[y+1][x+1] == 'x' else n
        return n
    else:
        return 'x'

