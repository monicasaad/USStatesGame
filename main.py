# import required modules
import turtle
import pandas

# global variables
FONT = ("Arial", 8, "normal")

# create screen object
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=750, height=525)

# create new turtle shap with picture of map
map_image = "blank_states_img.gif"
screen.addshape(map_image)
turtle.shape(map_image)

# create another turtle object to write correct guesses on screen
guess_writer = turtle.Turtle()
guess_writer.penup()
guess_writer.hideturtle()

# variable to keep track of score
correct_answers = 0
# variable to keep track of un-guessed states
states_left = 50

# read data from 50_states file
data = pandas.read_csv("50_states.csv")

# keep looping until user has guessed all states
while states_left > 0:
    # get user input for which state answer
    answer = screen.textinput(title=f"{correct_answers}/50 States Correct", prompt="Guess a state's name:")

    # convert answer to titlecase to match data in csv file
    tc_answer = answer.title()

    # check if user wants to exit game
    if answer == "Exit":
        break
    # check if answer is one of the 50 states
    for state in data.state:
        if tc_answer == state:
            correct_answers += 1
            states_left -= 1
            state_x = int(data[data.state == tc_answer].x)
            state_y = int(data[data.state == tc_answer].y)
            guess_writer.goto(state_x, state_y)
            guess_writer.write(state)

# keep screen open
turtle.mainloop()
