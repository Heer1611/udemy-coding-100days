from turtle import Screen
from snake_play import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True  
while game_on:
    screen.update()
    time.sleep(0.1) 
    snake.move()
    
    #detect collision with food
    if snake.head.distance(food) <15:
        food.new_food()
        snake.extand_snake()
        score_board.increase_score()
        
    #detect collision with wall
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_on = False
        score_board.end_game()

    #detect colliosion with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_on = False
            score_board.end_game()
            




screen.exitonclick()
