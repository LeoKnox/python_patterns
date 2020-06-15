def makeMap(len, width):
    for j in range(0, width):
        print('*',end="")
        for  i in range(0, len):
            print('.', end="")
        print('*')

makeMap(5,5)