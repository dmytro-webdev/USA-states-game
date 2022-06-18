from turtle import Turtle, Screen
#if you have an error - reinstall Pandas Package
import pandas


screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
bg = Turtle()
bg.shape(image)
screen.setup(width=725, height=491)


df = pandas.read_csv("50_states.csv")
start_title = "Guess the State"
states_correct = 0
states_list = []

while len(states_list) < 50:
    answer_state = screen.textinput(title=start_title, prompt="What's another state's name?").title()
    correct_guess = df.isin([f"{answer_state}"]).any().any()

    if answer_state == "Exit":
        break

    if answer_state not in states_list:
        if correct_guess:
            state = df[df["state"] == answer_state]
            text = Turtle()
            text.penup()
            text.goto(int(state.x), int(state.y))
            text.hideturtle()
            text.write(answer_state)
            states_correct += 1
            start_title = f"{states_correct}/50 States Correct"
            states_list.append(answer_state)

states_to_learn = df
# states to learn create a csv
for states in states_list:
    states_to_learn.drop(states_to_learn[states_to_learn.state == states].index, inplace=True)

states_to_csv = states_to_learn.state.to_list()

new_data = pandas.DataFrame(states_to_csv)
new_data.to_csv("States_to_learn.csv")







