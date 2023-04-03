from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle = Turtle()
turtle.shape(img)
guessed_states = []

data = pd.read_csv("50_states.csv")
#convert csv state to list
all_state = data.state.to_list()



m = Turtle()
m.hideturtle()  # to hide actual shape
m.penup()
m.goto(-35, -280)
m.write("This is for Education purpose made by VIKAS K.R.")




while len(guessed_states) < 50:
    ans_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                 prompt="What's another name?").title()

    if ans_state == "Exit":
        missing_states = []
        for state in all_state:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states_to_learn_m.csv")
        break

    if ans_state in all_state:
        guessed_states.append(ans_state)
        t = Turtle()
        t.hideturtle()  # to hide actual shape
        t.penup()
        v = data[data.state == ans_state]

        t.goto(int(v.x), int(v.y))
        # t.write(ans_state)
        t.write(v.state.item())





#screen.exitonclick() we have break statement so this line is not required