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