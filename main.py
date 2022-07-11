from turtle import Turtle, Screen
import random

rammus = Turtle()

rammus.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

directions = [0, 90, 180, 270]

rammus.pensize(15)
rammus.speed('fastest')

for _ in range(200):
    rammus.color(random_color())
    rammus.forward(30)
    rammus.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()

