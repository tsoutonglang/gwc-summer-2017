from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = -250
y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
t.pencolor("rosy brown")
t.forward(75)
t.left(140)
t.forward(50)
t.left(80)
t.forward(50)
t.penup()
t.right(-50)
t.pendown()
t.pencolor("aquamarine")
t.forward(75)
t.left(90)
t.forward(25)
t.left(90)
t.pencolor("coral")
t.forward(30)
t.right(90)
t.forward(25)
t.right(90)
t.forward(30)
# for Hunters in range(2):
t.right(90)
t.forward(25)
t.right(180)
t.forward(25)
t.pencolor("aquamarine")
# t.left(90)
t.forward(25)
t.left(90)
t.forward(75)
# Close window on click.
exitonclick()
