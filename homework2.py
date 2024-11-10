# Import Libraries
import pgzrun

WIDTH = 800
HEIGHT = 600
def draw():
    screen.clear()
    screen.fill('black')
    screen.draw.circle((100, 50), 80, 'green')
    screen.draw.line((150, 220), (400, 300), 'white')

def update():
    pass
pgzrun.go()