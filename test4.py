import random

class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def makeRoom(self):
        for k in range(0, self.width+2):
            print("*", end="")
        print()
        for j in range(0, self.length):
            print("*", end="")
            for i in range(0, self.width):
                print(".", end="")
            print("*")
        for k in range(0, self.width+2):
            print("*", end="")
        print()

    def newRoom(self):
        data = ["*", "."]
        x = random.choices(data, k=25)
        print(x)
    
    def testTest(self):
        x = [6, 4, 7, 3]
        print([i for i in x if i > x[len(x)-1]])
        x = [1, 3, 5]
        y = [1, 5]
        z = [(i,j) for i in x for j in y]
        #x = ["." for x in range(0, self.width, self.width-1) for y in range(self.length)]
        print(z)

r1 = Room(5,5)
r1.makeRoom()
r1.newRoom()
r1.testTest()