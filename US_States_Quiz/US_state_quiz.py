import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data= pandas.read_csv("50_states.csv")
all_state =data.state.to_list()
guessed_states =[]

while len (guessed_states) < 50: 
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's anoother state's name?").title()
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_state:
        guessed_states.append(answer_state)
        george = turtle.Turtle()
        george.hideturtle()
        george.penup()
        us_data = data[data.state == answer_state]
        george.goto(int(us_data.x), int(us_data.y)) 
        george.write(us_data.state.item())



