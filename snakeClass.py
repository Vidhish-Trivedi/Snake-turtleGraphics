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
        for pos in START_POS:
            self.add_part(pos)
            

    def move_snake(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[part_num - 1].xcor()
            new_y = self.parts[part_num - 1].ycor()
            self.parts[part_num].goto(new_x, new_y)
        # move head.
        self.head.forward(MOVE_DIST)

    # add a part to body.
    def add_part(self, pos):
        a = t.Turtle()
        a.penup()
        a.color("white")
        a.shape("square")
        a.goto(pos)
        self.parts.append(a)
    
    # extend body by adding a part at the end of snake body.
    def extend(self):
        self.add_part(self.parts[-1].position())  # get a hold of position of last part of snake body.

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