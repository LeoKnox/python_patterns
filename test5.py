import random, math

class Level:
    x_list = []

    def __init__(self):
        pass

    def show(self):
        for i in self.x_list:
            print(i)

    def rn(self, x=8):
        random.seed(x)
        print(random.random())
        random.seed(x+1)
        print(random.random())
        random.seed(x)
        print(random.random())
        return(math.floor(random.random()*10))

    def build(self):
        self.x_list.append(self.rn())

x = [4,6,9,1]
l = Level()
l.show()
l.build()
l.show()