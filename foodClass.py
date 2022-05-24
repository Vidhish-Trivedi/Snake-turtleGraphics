# create red food, detect collisions in snake.py.
import turtle as t
import random


# Food class inherits from the Turtle class.
class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)  # scaling the circle by half.
        self.speed(0)
        # put at a random point on screen.
        self.regen()

    def regen(self):
        # put at a random point on screen.
        r_x = random.randint(-280, 280)
        r_y = random.randint(-280, 280)
        self.goto(r_x, r_y)

        
