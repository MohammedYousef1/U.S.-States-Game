import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725 , height=491)
image_path = "C:/Users/user/Desktop/Angela course/U.S. states game/blank_states_img.gif" # Path of the gif file
screen.addshape(image_path) # Background
turtle.shape(image_path) # Background
data = pandas.read_csv("C:/Users/user/Desktop/Angela course/U.S. states game/50_states.csv") # Path of the csv file

all_states = data.state.to_list() # Insert the states to list called (all_states)

counter_correct_answers = 0 # counter for correct answer

while(counter_correct_answers <= 50):
    answer_state = screen.textinput(title=f"{counter_correct_answers}/50 Correct State" , prompt="Enter the state here:").title()

    if(answer_state == "Exit"):
        break

    if answer_state in all_states:
        X = data[data.state == answer_state].x.item() # Get X axis from the csv file
        X = data[data.state == answer_state].y.item() # Get Y axis from the csv file
        t = turtle.Turtle() # New Turtle
        t.penup() # penup() to get the pun so when the turtle move he dont type on the screen
        t.hideturtle() # Hide the turtle
        t.setposition(X,Y) # Set Position on the screen using X and Y
        t.write(answer_state) # Write the state on the X and Y position on the screen
        all_states.remove(answer_state) # Delete the answer_state from the list so the user don't type it again
        counter_correct_answers += 1 # increase counter by one

# If the user type Exit, we convert the rest of the list (all_states) to csv and call it missing_states, so he can learn them later.
new_data = pandas.DataFrame(data=all_states)
new_data.to_csv("missing_states.csv")