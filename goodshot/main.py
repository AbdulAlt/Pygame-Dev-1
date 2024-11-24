# importing libraries
import pgzrun
import random

# output properties
TITLE = 'Shoot The Alien'
WIDTH = 500
HEIGHT = 500

# initializing message, alien, and score
message = 'shoot it.'
alien = Actor('alien')
score = 0

# pop function that plays the pop sound
def pop_sound():
    music.play('song')

# song function that plays the song
def song():
    pass

# draw function to render the game scene
def draw():
    screen.clear()
    screen.fill(color=(0, 0, 200))  # Set background color
    alien.draw()  # Draw the alien at the center
    screen.draw.text(message, center=(250, 10), fontsize=30)  # Display the score

# place alien in the center of the screen
def place_alien():
    alien.x = random.randint(50, WIDTH - 50)
    alien.y = random.randint(50, HEIGHT - 50)

# on_mouse_down function to handle mouse clicks
def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):  # Check if the click is on the alien
        score += 1  # Increment the score
        message = f'score: {score}'
        pop_sound()
        place_alien()  # Keep the alien in the center
    else:
        score -= 1  # Decrement the score
        message = f'score: {score}'

# Stuff
song()
place_alien()
pgzrun.go()