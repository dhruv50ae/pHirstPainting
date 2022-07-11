from turtle import Turtle, Screen
import random

rammus = Turtle()
directions = [0, 90, 180, 270]
rammus.speed('fastest')

def drawSpiro(sizeOfGap):
    for _ in range(int(360/sizeOfGap)):
        rammus.circle(100)
        rammus.setheading(rammus.heading()+sizeOfGap)

drawSpiro(5)

screen = Screen()
screen.exitonclick()

