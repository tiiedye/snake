# Snake project
import turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = turtle.Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


# All code before exit
screen.exitonclick()
