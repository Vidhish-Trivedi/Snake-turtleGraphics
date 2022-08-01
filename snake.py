# Build Snake game using turtle graphics.
import turtle as t
import time
from snakeClass import Snake
from foodClass import Food
from scoreClass import Score

t.colormode(255)  # set color mode to accept values in range 0 to 255.
screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor(54, 174, 124)  # set background color.
screen.title("......sNaKe......")

# create snake body.
mySnake = Snake()
# initialise food.
food = Food()
# initialise scoreboard.
scoreBoard = Score()

screen.tracer(0)  # turn off animations.
screen.listen()
# listen for key presses to move snake accordingly.
screen.onkey(key = "Up", fun = mySnake.up)
screen.onkey(key = "Down", fun = mySnake.down)
screen.onkey(key = "Left", fun = mySnake.turn_left)
screen.onkey(key = "Right", fun = mySnake.turn_right)

# moving the snake automatically, continuously.
run = True
while(run):
    # since animations (screen.tracer(0) --> off) are off, we need to manually refresh screen.
    screen.update()
    time.sleep(0.1)
    
    mySnake.move_snake()

    # detect collisions with wall.
    if(mySnake.head.xcor() > 295 or mySnake.head.xcor() < -301 or mySnake.head.ycor() > 300 or mySnake.head.ycor() < -295):
        # run = False
        scoreBoard.reset_score()
        mySnake.reset_snake()

    # detect collision with tail.
    # head colliding with any part of snake body.
    for part in mySnake.parts[1:]:  # ignore collision of head with itself.
        if(mySnake.head.distance(part) < 10):
            # run = False
            scoreBoard.reset_score()
            mySnake.reset_snake()

    # detect collisions with food.
    if(mySnake.head.distance(food) < 15):
        # print("score!")
        food.regen()
        mySnake.extend()
        scoreBoard.increment()

    if(run == False):
        print("game over......")  # print to terminal.

screen.exitonclick()
