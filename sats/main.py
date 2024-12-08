# importing libraries
import pgzrun
import random
from random import randint

# settings
TITLE = 'Game'
WIDTH = 800
HIEGHT = 600

# variables
sl = []
lines = []
next_sat = 0
num_of_sats = 8

# create sats
def create_sats():
    for i in range(8):
        sats = Actor('spr_sat')
        sats.pos = (randint(40, WIDTH - 40), randint(40, HEIGHT - 40))
        sl.append(sats)

# draw function
def draw():
    # draw background
    screen.blit('spr_bg'(0, 0))
    # number of sats
    num = 1
    for i in sl:
        screen.draw.text(str(num), (sat.pos[0], sat.pos[1] + 20))
        sats.draw()
        num += 1

# calling functions
create_sats()
pgzrun.go()