# importing libraries
import pgzrun
import random

# output properties
TITLE = 'Shoot The Alien'
WIDTH = 500
HEIGHT = 500

# drawing stuff part 1
message = 'start the game by shooting'
alien = Actor('alien')

# draw functon
def draw():
    screen.clear()
    screen.fill(color = (0, 0, 200))
    alien.draw()
    screen.draw.text(message, center = (250, 10), fontsize = 30)

# place alien function
def place_alien():
    alien.x = random.randint(50, WIDTH - 50)
    alien.y = random.randint(50, HEIGHT - 50)

# on_mouse_down
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = 'good shot'
        place_alien()
    else:
        message = 'you missed'

# calling functions
place_alien()

pgzrun.go()