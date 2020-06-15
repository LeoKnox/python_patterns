import random

def makeMap(len, width):
    for j in range(0, width):
        z = random.random()*10
        print('*',end="")
        if z // 2 == 1:
            print('..', end='')
        for  i in range(0, len):
            print('.', end="")
        print('*')

makeMap(5,5)