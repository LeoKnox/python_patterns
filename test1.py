import random

def makeMap(len, width):
    for j in range(0, width):
        z = random.random()*15
        print('*',end="")
        if z < 6:
            len -= 1
        elif z < 10:
            len += 1
        for  i in range(0, len):
            print('.', end="")
        print('*')

makeMap(5,5)