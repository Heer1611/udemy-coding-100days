import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [ (142, 77, 52), (188, 165, 118), (165, 152, 38), (16, 46, 83), (46, 110, 135), 
 (144, 57, 83), (61, 120, 100), (143, 184, 174), (141, 170, 176), (86, 36, 30), 
 (65, 152, 168), (219, 209, 96), (109, 38, 32), (102, 145, 110), (166, 98, 130), 
 (95, 122, 169), (161, 140, 160), (176, 104, 84), (52, 52, 87), (206, 182, 195), 
 (67, 47, 63), (75, 51, 67), (174, 200, 193), (171, 200, 203), (217, 180, 172), (182, 191, 206)]

tim.setheading(225)
tim.forward(400)
tim.setheading(0)
number_dots = 131


for dot_total in range(1,number_dots):
    tim.dot(20,random.choice(color_list))
    tim.fd(50)
    if dot_total %10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()