from turtle import Turtle, Screen

rammus = Turtle()

rammus.shape("turtle")
rammus.color("purple")

for _ in range(4):
    rammus.forward(100)
    rammus.right(90)

# rammus.forward(100)
# rammus.right(90)
# rammus.forward(100)
# rammus.right(90)
# rammus.forward(100)
# rammus.right(90)
# rammus.forward(100)
# rammus.right(90)

screen = Screen()
screen.exitonclick()

