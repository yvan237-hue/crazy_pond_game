from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.initial_score_l = 0
        self.initial_score_r = 0

    def updated_score(self):
        self.clear()
        self.goto(-100,230)
        self.write(self.initial_score_l, align="center", font=("Tahoma", 24, "bold"))
        self.goto(100, 230)
        self.write(self.initial_score_r, align="center", font=("Tahoma", 24, "bold"))
    def left_score(self):
        self.initial_score_l += 1
        self.updated_score()


    def right_score(self):
        self.initial_score_r += 1
        self.updated_score()

