# importing libraries
import pgzrun
from random import randint
from time import time

# settings
TITLE = 'Game'
WIDTH = 800
HIEGHT = 600

# variables
sl = []
lines = []
next_sat = 0
num_of_sats = 8

start_time = 0
total_time = 0
end_time = 0
# create sats
def create_sats():
    global start_time
    for i in range(8):
        sats = Actor('spr_sat')
        sats.pos = (randint(40, WIDTH - 40), randint(40, HIEGHT - 40))
        sl.append(sats)
        start_time = time()

# draw function
def draw():
    global total_time
    # draw background
    screen.blit('spr_bg', (0, 0))
    # number of sats
    num = 1
    for i in sl:
        screen.draw.text(str(num), (i.pos[0], i.pos[1] + 20))
        i.draw()
        num += 1

    for i in lines:
        screen.draw.line(i[0], i[1], (255, 255, 255))
        if next_sat < num_of_sats:
            total_time = time() - start_time
            screen.draw.text(str(time), (10, 10), fontsize = 30)
        else:
            screen.draw.text(str(time), (10, 10), fontsize = 30)
    def on_mouse_down(pos):
        global next_sat, lines
        if next_sat < num_of_sats:
            if sl[next_sat].collidepoint(pos):
                if next_sat:
                    lines.append(sl[next_sat - 1].pos, sl[next_sat.pos])
                    next_sat += 1
                else:
                    lines = []
                    next_sat = 0
def update():
    pass


# calling functions
create_sats()
pgzrun.go()
