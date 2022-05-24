# Build Snake game using turtle graphics.
import turtle as t
import time
from snakeClass import Snake
from foodClass import Food
from scoreClass import Score

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
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
    if(mySnake.head.xcor() > 281 or mySnake.head.xcor() < -281 or mySnake.head.ycor() > 281 or mySnake.head.ycor() < -281):
        run = False
        scoreBoard.game_over()

    # detect collisions with food.
    if(mySnake.head.distance(food) < 15):
        # print("score!")
        food.regen()
        scoreBoard.increment()

    if(run == False):
        print("game over......")

screen.exitonclick()
