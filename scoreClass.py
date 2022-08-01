import turtle as t
ALIGNMENT = "center"
FONT = ("algerian", 20, "normal")

class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Read High Score saved on machine.
        with open('./HS.txt') as hs:
            h_score = hs.read()
            self.high_score = int(h_score)  # To keep track of high score.
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
            # Update High Score saved in a file.
            with open('./HS.txt', mode='w') as hs:
                hs.write(str(self.score))

        self.score = 0
        self.update_board()


