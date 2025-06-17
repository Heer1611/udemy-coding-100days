from operator import iand
from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make you bet", prompt= "which turtle will win the race? Enter a color: ")
print (user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100,-70,-40, -10 , 20, 50]
all_turtle = []

for turtle_index in range(0,5):
    new_turtle = Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_pos[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True
while race_on: 
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
            
            
        rand_dis = random.randint(0,10)
        turtle.fd(rand_dis)
        

screen.exitonclick()