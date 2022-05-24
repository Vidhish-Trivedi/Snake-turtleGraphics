# Build Snake game using turtle graphics.
import turtle as t
import random, time
from snakeClass import Snake

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("......sNaKe......")
# turn off animations.
screen.tracer(0)
screen.listen()

# create snake body.
mySnake = Snake()

#########################################################################################################

# IMPLEMENTED IN SNAKE CLASS.

# create 3 squares(turtles) in a row.  (cba) ==> 'a' is head, at (0, 0). 

# start_pos = [(0, 0), (-20, 0), (-40, 0)]
# parts = []

# for p in start_pos:
#     a = t.Turtle()
#     a.penup()
#     a.color("white")
#     a.shape("square")
#     a.goto(p)
#     parts.append(a)
#########################################################################################################
# IMPLEMENTED IN SNAKE CLASS.
# def turn_left():
#     parts[0].left(90)

# def turn_right():
#     parts[0].right(90)
#########################################################################################################
# moving the snake automatically, continuously.
run = True
while(run):
    # since animations (screen.tracer(0) --> off) are off, we need to manually refresh screen.
    screen.update()
    time.sleep(0.1)
    
    mySnake.move_snake()

    # IMPLEMENTED IN SNAKE CLASS.
    # moving segments other than head
    # for part_num in range(len(parts) - 1, 0, -1):
    #     new_x = parts[part_num - 1].xcor()
    #     new_y = parts[part_num - 1].ycor()
    #     parts[part_num].goto(new_x, new_y)
    # # move head.
    # parts[0].forward(20)

    screen.onkey(key = "Up", fun = mySnake.up)
    screen.onkey(key = "Down", fun = mySnake.down)
    screen.onkey(key = "Left", fun = mySnake.turn_left)
    screen.onkey(key = "Right", fun = mySnake.turn_right)

screen.exitonclick()