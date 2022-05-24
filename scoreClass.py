import turtle as t
ALIGNMENT = "center"
FONT = ("algerian", 20, "normal")

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER.....", align = ALIGNMENT, font = FONT)
