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
        display_msg('Game over', 'try again!')
    elif game_complete:
        display_msg('You won', 'well done!')
    else:
        for i in items:
            i.draw()

# update function
def update():
    global items
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
def get_option_to_create(num_of_extra_items):
    items_to_create = ['paper']
    for i in range(0, num_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

# create item function
def create_item(items_to_create):
    new_items = []
    for i in items_to_create:
        items = Actor(i + 'img')
        new_items.append(items)
    return new_items

# layout items function
def layout_items(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / num_of_gaps
    random.shuffle(items_to_layout)
    for index, items in enumerate(items_to_layout):
        x_pos = (index + 1) * gap_size
        items.x = x_pos



# animate items function
def animate_items(items_to_animate):
    global animation
    for i in items_to_animate:
        duration = START_SPEED - current_lv
        i.anchor = ('center', 'bottom')
        animation = animate(i, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

# handle_game_over function
def handle_game_over():
    global game_over
    game_over = True

# on mouse down function
def on_mouse_down(pos):
    for i in items:
        if i.collidepoint(pos):
            if 'paper' in i.image:
                handle_game_complete()
            else:
                handle_game_over()

# handle game complete function
def handle_game_complete():
    global current_lv, items, animations, game_complete
    stop_animations(animations)
    if current_lv == FINAL_LV:
        game_complete = True
    else:
        current_lv += 1
        items = []
        animations = []

# stop animation function
def stop_animations(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()

# display message function
def display_msg(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 60, center = CENTER, color = 'white')
    screen.draw.text(sub_heading_text, fontsize = 30, center = (WIDTH / 2, HEIGHT / 2 + 30), color = 'white')

pgzrun.go()
