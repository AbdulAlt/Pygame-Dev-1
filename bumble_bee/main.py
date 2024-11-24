# import libraries
import pgzrun
import random

# width and height
TITLE = 'bumble bee'
WIDTH = 600
HEIGHT = 500

# creating variables
score = 0
game_over = False
bee = Actor('bee')
flower = Actor('flower')
bee.pos = 100, 100
flower.pos = 200, 200

# draw function
def draw():
    screen.blit('bg', (0, 0))
    bee.draw()
    flower.draw()
    screen.draw.text('score: {}'.format(score), color = 'black', topleft = (10, 10))
    # game over code
    if game_over:
        screen.fill('pink')
        screen.draw.text('game over!', color = 'red', midtop = (WIDTH / 2, 10), fontsize = 40)

# place flower function
def place_flower():
    flower.x = random.randint(70, WIDTH - 70)
    flower.y = random.randint(70, HEIGHT - 70)

# time up function
def time_up():
    global game_over
    game_over = True

# update function
def update():
    global score
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.down:
        bee.y += 2
    if keyboard.up:
        bee.y -= 2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score += 10
        place_flower()


clock.schedule(time_up, 60)
pgzrun.go()