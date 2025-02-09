# import libraries
import pgzrun
import random

# settings
TITLE = "Golaga Game"
WIDTH = 1200
HEIGHT = 600

# variables
ship = Actor("ship")
speed = 5
bug = Actor("bug")
ship.pos = (600, HEIGHT - 60)
bullets = []
enemies = []
enemies.append(Actor("bug"))
enemies[-1].x = 10
enemies[-1].y = -100
score = 0

# display score function
def display_score():
    global score
    screen.draw.text(str(score), (50, 30))

# fire bullets function
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("bullet"))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y - 50
        sounds.eep.play()


# draw function
def draw():
    screen.clear()
    screen.fill("blue")
    for i in bullets:
        i.draw()
    for j in enemies:
        j.draw()
    ship.draw()
    display_score()

# update function
def update():
    global score
    if keyboard.left:
        ship.x -= speed
        if ship.x <= 0:
            ship.x = 0
    elif keyboard.right:
        ship.x += speed
        if ship.x >= WIDTH:
            ship.x = WIDTH
    for i in bullets:
        if i.y <= 0:
            bullets.remove(i)
        else:
            i.y -= 10
    for j in enemies:
        j.y += 5
        if j.y >= HEIGHT:
            j.x = random.randint(50, WIDTH - 50)
            j.y = -100
        for i in bullets:
            if j.colliderect(i):
                score += 100
                bullets.remove(i)
                enemies.remove(j)


pgzrun.go()
