import pandas
import turtle
from turtle import Turtle, Screen

screen = Screen()

image = "blank_states_img.gif"
screen.addshape(image)
map = Turtle(image)
text_turtle = Turtle()
text_turtle.hideturtle()
screen.setup(width=725, height=491)
total = 50
correct = 0

data = pandas.read_csv("50_states.csv")


prompt = turtle.textinput("Guess", f"Score: {correct}/{total} States")

states_list = (data["state"].str.lower().tolist())
state_x_cor = (data["x"].tolist())
state_y_cor = (data["y"].tolist())

while prompt:

    found = False
    prompt_lower = prompt.lower()

    for i in range(len(states_list)):

        if states_list[i] == prompt_lower:
            text_turtle.hideturtle()
            text_turtle.penup()
            text_turtle.goto(state_x_cor[i], state_y_cor[i])
            text_turtle.write(prompt, align="Center", font=("Arial", 8, "normal"))
            found = True
            correct += 1
            break

    prompt = turtle.textinput(f"Guess", f"Score: {correct}/{total} States")



screen.mainloop()