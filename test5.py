import random

class Level:
    x_list = []

    def __init__(self):
        pass

    def show(self):
        for i in self.x_list:
            print(i)

x = [4,6,9,1]
l = Level()
l.show()