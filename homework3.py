# importing libraries
from random import randint
import pgzrun
import time

# setting the width and heigh
WIDTH = 800
HEIGHT = 600

# draw function
def draw():
    for i in range(500):
        x = randint(0, 800)
        y = randint(0, 600)
        width = randint(0, 400)
        height = randint(0, 300)
        rect = Rect((x, y), (width, height))
        screen.draw.rect(rect, 'blue')
        width -= 10
        height += 10

# output window
pgzrun.go()