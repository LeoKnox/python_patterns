import random, math

class Level:
    x_list = []

    def __init__(self):
        pass

    def show(self):
        for i in self.x_list:
            print(i)

    def rn(self, x=8):
        return(math.floor(random.random()*x))

    def build(self):
        self.x_list.append(self.rn())

x = [4,6,9,1]
l = Level()
l.show()
l.build()
l.show()