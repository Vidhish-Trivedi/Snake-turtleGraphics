import turtle as t
ALIGNMENT = "center"
FONT = ("algerian", 20, "normal")

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0  # To keep track of high score for a session.
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def increment(self):
        self.score += 1
        self.update_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write("GAME OVER", align = ALIGNMENT, font = FONT)

    def update_board(self):
        self.clear()
        self.write(f"Score : {self.score} | High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset_score(self):
        if(self.score > self.high_score):
            self.high_score = self.score
        self.score = 0
        self.update_board()


