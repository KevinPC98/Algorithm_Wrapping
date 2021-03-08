from wrapping import *
import random
if __name__ == '__main__':
    #To consider: random.sample(range(Begin,End),(End-Begin))
    x = random.sample(range(-20, 10), 30)
    y = random.sample(range(-20, 10), 30)
    w = Wrapping(x,y)
    w.Main()
