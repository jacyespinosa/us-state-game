import turtle
import pandas

screen = turtle.Screen()
screen.title("Jacy's U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

user_input = screen.textinput(title="Guess the State", prompt="What's the state's name?").title()

data = pandas.read_csv("50_states.csv")
correct_guess = []

while len(correct_guess) < len(data["state"]):
    if user_input == "Exit":
        break

    if len(correct_guess) == len(data["state"]) - 1:
        turtle.penup()
        turtle.goto(0,0)
        turtle.pendown()
        turtle.pencolor("red")
        turtle.write(arg="CONGRATULATIONS! YOU'VE GUESS THEM ALL RIGHT!!!", align="center", font=("Arial", 30, "normal"))

    elif user_input not in data["state"].to_list():
        user_input = screen.textinput(title=f"{len(correct_guess)+1}/50 States Correct",
                                          prompt="WRONG! Try another state name.").title()
    elif user_input in correct_guess:
        user_input = screen.textinput(title=f"{len(correct_guess) + 1}/50 States Correct",
                                      prompt="Already guessed. Name another state.").title()


    elif user_input in data["state"].to_list():
        which_state = data[data.state == user_input]
        x_cor = int(which_state.x)
        y_cor = int(which_state.y)
        t = turtle.Turtle()
        t.pencolor("black")
        t.penup()
        t.hideturtle()
        t.goto(x_cor, y_cor)
        t.write(arg=user_input, font=("Arial", 10, "normal"))
        correct_guess.append(user_input)
        user_input = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name?").title()


#SAVE THE MISSING STATES TO A NEW FILE: states_to_learn.csv
states_to_learn = []
for state in data["state"].to_list():
    if state not in correct_guess:
        states_to_learn.append(state)

new_data = pandas.DataFrame(states_to_learn)
new_data.to_csv("states_to_learn.csv")
