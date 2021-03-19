def printGameLayout(gameDataLayout: list):
    print('---------------------------\n')
    for line in gameDataLayout:
        c = []
        for e in line:
            c.append(str(e))
        string = ' | '.join(c)
        print(string)
        print('-' * len(string))
    
    print('---------------------------\n')