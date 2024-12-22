# importing libraries
import pgzrun
from random import randint
from time import time

# settings
TITLE = 'Game'
WIDTH = 800
HEIGHT = 600  # Fixed spelling

# variables
sl = []
lines = []
next_sat = 0
num_of_sats = 8

start_time = 0
total_time = 0

# create sats
def create_sats():
    global start_time
    for i in range(num_of_sats):
        sats = Actor('spr_sat')
        sats.pos = (randint(40, WIDTH - 40), randint(40, HEIGHT - 40))
        sl.append(sats)
    start_time = time()  # Start the timer after satellites are created

# draw function
def draw():
    global total_time
    # draw background
    screen.blit('spr_bg', (0, 0))

    # draw satellites and their numbers
    num = 1
    for sat in sl:
        screen.draw.text(str(num), (sat.pos[0], sat.pos[1] + 20))
        sat.draw()
        num += 1

    # draw connection lines
    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))

    # display time
    if next_sat < num_of_sats:
        total_time = time() - start_time
    screen.draw.text(f'Time: {total_time:.2f}s', (10, 10), fontsize=30)

# handle mouse clicks
def on_mouse_down(pos):
    global next_sat, lines
    if next_sat < num_of_sats:
        if sl[next_sat].collidepoint(pos):
            if next_sat > 0:  # Connect to the previous satellite
                lines.append((sl[next_sat - 1].pos, sl[next_sat].pos))
            next_sat += 1
        else:
            lines = []  # Reset lines if a wrong satellite is clicked
            next_sat = 0

# update function (no updates needed currently)
def update():
    pass

# calling functions
create_sats()
pgzrun.go()
