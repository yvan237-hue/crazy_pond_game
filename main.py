from turtle import Screen
from paddle import Paddle
from pong_ball import PongBall
from  score import ScoreBoard
import time

screen = Screen()
screen.title("Crazy Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor('black')
gaming = True
screen.listen()
screen.tracer(0)

left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))
screen.onkey(left_paddle.move_paddle_up, "Up")
screen.onkey(left_paddle.move_paddle_down, "Down")

screen.onkey(right_paddle.move_paddle_up, "z")
screen.onkey(right_paddle.move_paddle_down, "s")

ball = PongBall()
all_score = ScoreBoard()
all_score.updated_score()

while gaming:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(left_paddle) < 40 and ball.xcor() < -320 or ball.distance(right_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() < -380 :
        ball.reset()
        all_score.right_score()

    if ball.xcor() > 380 :
        ball.reset()
        all_score.left_score()



screen.exitonclick()


"""Good bye and happy Sunday 
            By Mr Py //
            Contact :+237 671418204 
"""