# import libraries
import pgzrun
import random

# settings and constants
TITLE = 'Recycle Game'
WIDTH = 800
HEIGHT = 600
CENTER = (WIDTH / 2, HEIGHT / 2)
FINAL_LV = 6
START_SPEED = 10
ITEMS = ['bag', 'battery', 'bottle', 'chips']

# variables
game_over = False
game_complete = False
current_lv = 1
paper = Actor('paperimg')
items = []
animations = []

# draw function
def draw():
    global game_over, game_complete, items
    screen.clear()
    screen.blit('bground', (0, 0))
    if game_over:
        display_msg('Game over, try again')
    elif game_complete:
        display_msg('You won, well done!')
    else:
        for i in items:
            i.draw()

# update function
def update():
    if len(items) == 0:
        items = make_items(current_lv)

# make items function
def make_items(num_of_extra_items):
    items_to_create = get_option_to_create(num_of_extra_items)
    new_items = create_item(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

# get option to create function
def get_option_to_create():
    pass

# layout items function
def layout_items():
    pass

# handle_game_over function
def handle_game_over():
    pass

# animate items function
def animate_items():
    pass

# create item function
def create_item():
    pass

# on mouse down function
def on_mouse_down():
    pass

# handle game complete function
def handle_game_complete():
    pass

# stop animation function
def stop_animations():
    pass

# display message function
def display_msg():
    pass
