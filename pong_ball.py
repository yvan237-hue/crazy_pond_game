from turtle import Turtle

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color("red")
        self.goto(0, 0)
        self.move_factor_x = 10
        self.move_factor_y = 10
        self.ball_speed = 0.1

    def move_ball(self):
        self.goto(self.xcor()+self.move_factor_x, self.ycor()+self.move_factor_y)

    def bounce_x(self):
        self.move_factor_x *= -1
        self.ball_speed *= 0.9

    def bounce_y(self):
        self.move_factor_y *= -1

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()




