# Import Libraries
import pgzrun

WIDTH = 800
HEIGHT = 600
def draw():
    screen.clear()
    screen.fill('red')
    screen.draw.circle((100, 100), 80, 'green')
    screen.draw.line((100, 300), (400, 300), 'white')
    rect = Rect((50,100), (100, 150))
    screen.draw.filled.rect(rect, 'blue')

def update():
    pass
pgzrun.go()