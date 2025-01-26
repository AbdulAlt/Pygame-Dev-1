# importing libraries
import pgzrun
import random

# settings
WIDTH = 900
HEIGHT = 850
TITLE = 'Quiz Master'

# box variables
marque_box = Rect(0, 0, 700, 80)
question_box = Rect(0, 0, 650, 150)
timer_box = Rect(0, 0, 150, 150)
answer_box_1 = Rect(0, 0, 300, 150)
answer_box_2 = Rect(0, 0, 300, 150)
answer_box_2 = Rect(0, 0, 300, 150)
answer_box_3 = Rect(0, 0, 300, 150)
answer_box_4 = Rect(0, 0, 300, 150)
skip_box = Rect(0, 0, 200, 380)

# other variables
score = 0
time_left = 10
question_file = 'questions.txt'
marque_msg = ''
is_gameover = False
answer_boxes = [answer_box_1, answer_box_2, answer_box_3, answer_box_4]
questions = []
questions_count = 0
question_index = 0

# placing boxes
marque_box.move_ip(0, 0)
question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box_1.move_ip(20, 270)
answer_box_2.move_ip(370, 270)
answer_box_3.move_ip(20, 450)
answer_box_4.move_ip(370, 450)
skip_box.move_ip(700, 270)

# draw function
def draw():
    # clear screen
    screen.clear()
    # fill screen with the black colour
    screen.fill(color = 'black')
    # draw the marque box
    screen.draw.filled_rect(marque_box, 'black')
    # draw the question box
    screen.draw.filled_rect(question_box, 'navy blue')
    # draw the timer box
    screen.draw.filled_rect(timer_box, 'navy blue')
    # draw the skip box
    screen.draw.filled_rect(skip_box, 'dark green')

    # draw the answer boxes loop
    for i in answer_boxes:
        screen.draw.filled_rect(i, 'dark orange')

    # marque message
    marque_msg = f'welcom to Quiz Master---?{question_index} of {questions_count}'
    # draw the marque
    screen.draw.textbox(marque_msg, marque_box, color = 'white')
    # draw the timer
    screen.draw.textbox(str(time_left), timer_box, color = 'white')
    # draw the skip button
    screen.draw.textbox('skip', skip_box, color = 'black', angle = -90)

# read question file function
def read_question_file():
    # global the variables
    global question_file, questions, questions_count
    # create a variable for the question files
    q_file = open(question_file, 'r')
    for i in q_file:
        questions.append(i)
        questions_count += 1
    q_file.close()

# read next question function
def read_next_question():
    global question_index
    question_index += 1
    return questions.pop(0).split(",")

# update function
def update():
    mov_marque()

# move marque function
def mov_marque():
    marque_box.x -= 2
    if marque_box.right < 0:
        marque_box.left = WIDTH

# on mouse down function
def on_mouse_down(pos):
    index = 1
    for i in answer_boxes:
        if i.collidepoint(pos):
            if index is int(x[5]):
                correct_answer()
            else:
                game_over()
        index += 1
    if skip_box.collidepoint(pos):
        skip_question()

# correct answer function
def correct_answer():
    global score, time_left
    score += 1
    if questions:
        x = read_next_question()
        time_left = 10
    else:
        game_over()

# skip question function
def skip_question():
    global time_left, x, is_gameover
    if x and not is_gameover:
        x = read_next_question()
        time_left = 10

# game over function
def game_over():
    global x,time_left, is_gameover
    msg = f'Game over! You got {score} questions correct.'
    x = [msg, '-', '-', '-', '-', '-', 5]
    time_left = 0
    is_gameover = True

# update time left function
def update_time_left():
    global time_left
    if time_left:
        time_left -= 1
    else:
        game_over()

# call functions
read_question_file()
x = read_next_question()
print(x)
clock.schedule_interval(update_time_left, 1)
pgzrun.go()
