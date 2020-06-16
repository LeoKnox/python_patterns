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
        x = ["." for x in range(0, self.width, self.width-1) for y in range(self.length)]
        print(x)

r1 = Room(5,5)
r1.makeRoom()
r1.newRoom()