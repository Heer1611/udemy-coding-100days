from turtle import Screen
from pong_paddle import paddles
from ball import Ball
from pong_score import Scorebord  
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

user_1 = paddles((350, 0))
user_2 = paddles((-350, 0))
ball = Ball()
scoreboard = Scorebord()  

screen.listen()
screen.onkey(user_1.go_up, "Up")
screen.onkey(user_1.go_down, "Down")
screen.onkey(user_2.go_up, "w")  
screen.onkey(user_2.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Collision with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with paddles
    if (ball.distance(user_1) < 50 and ball.xcor() > 320) or (ball.distance(user_2) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Ball out of bounds
    if ball.xcor() > 380:
        scoreboard.left_point()
        ball.reset_pos()

    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset_pos()

screen.exitonclick()
