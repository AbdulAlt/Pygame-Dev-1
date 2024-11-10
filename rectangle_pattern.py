# Importing libraries
import pgzrun
from random import randint

# Setting the width and height
WIDTH = 300
HEIGHT = 300

# Using the draw funciton
def draw():
    width = WIDTH
    height = HEIGHT - 200
    r = 255
    g = 0
    b = randint(120, 255)
    screen.clear()
    for i in range(20):
        rect = Rect((150, 150), (width, height))
        screen.draw.rect(rect, (r, g, b))
        r -= 10
        b += 20
        width -= 10
        height -= 10


# Update the screen
def update():
    pass

# Hold the output screen
pgzrun.go()