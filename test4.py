class Room:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def makeRoom(self):
        for i in range(0, self.width):
            print(".", end="")

r1 = Room(5,5)
r1.makeRoom()