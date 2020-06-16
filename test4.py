class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def makeRoom(self):
        for j in range(0, self.length):
            print("*", end="")
            for i in range(0, self.width):
                print(".", end="")
            print("*")
        print("*")

r1 = Room(5,5)
r1.makeRoom()