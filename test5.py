import random

class Level:
    def __init__(self, x_list):
        self.x_list = x_list

    def show(self):
        for i in self.x_list:
            print(i)

x = [4,6,9,1]
l = Level(x)
l.show()