import turtle as t

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20

# Create Snake class for snake game.
class Snake:
    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for p in START_POS:
            a = t.Turtle()
            a.penup()
            a.color("white")
            a.shape("square")
            a.goto(p)
            self.parts.append(a)

    def move_snake(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part_num - 1].xcor()
            new_y = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(new_x, new_y)
        # move head.
        self.head.forward(MOVE_DIST)

    def up(self):
        if(self.head.heading() != 270):
            self.head.setheading(90)

    def down(self):
        if(self.head.heading() != 90):
            self.head.setheading(270)

    def turn_left(self):
        if(self.head.heading() != 0):
            self.head.setheading(180)
    
    def turn_right(self):
        if(self.head.heading() != 180):
            self.head.setheading(0)