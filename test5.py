import random

class Level:
    x_list = []

    def __init__(self):
        pass

    def show(self):
        for i in self.x_list:
            print(i)
    
    def build(self):
        self.x_list.append(7)

x = [4,6,9,1]
l = Level()
l.show()
l.build()
l.show()