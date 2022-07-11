from turtle import Turtle, Screen

rammus = Turtle()


def drawShape(numSides):
    angle = 360/numSides
    for _ in range(numSides):
        rammus.forward(100)
        rammus.right(angle)

for shapeSideN in range(3, 11):
    drawShape(shapeSideN)

screen = Screen()
screen.exitonclick()

