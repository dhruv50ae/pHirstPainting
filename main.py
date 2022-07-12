import colorgram

# colours = colorgram.extract('975994.jpg', 30)
# rgbColours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     newColour = (r, g, b)
#     rgbColours.append(newColour)
# print(rgbColours)

import turtle as turtleModule
import random

turtleModule.colormode(255)
rammus = turtleModule.Turtle()
rammus.hideturtle()
rammus.penup()
rammus.speed('fastest')

colourList = [(25, 15, 12), (220, 229, 238), (91, 93, 98), (46, 41, 43), (153, 160, 170), (254, 254, 254), (50, 50, 53), (82, 78, 76), (82, 78, 80), (248, 254, 253), (182, 191, 202), (62, 62, 67), (122, 127, 135), (67, 61, 64), (251, 249, 251), (82, 85, 84), (72, 60, 57), (34, 37, 35), (156, 151, 147), (152, 145, 149), (66, 64, 59), (150, 155, 153), (133, 124, 129), (114, 132, 138), (53, 67, 71), (140, 122, 119), (174, 197, 206), (60, 66, 60), (131, 128, 121), (202, 185, 189)]

rammus.setheading(225)
rammus.forward(300)
rammus.setheading(0)
numberOfDots = 100

for dotCount in range(1, numberOfDots + 1):
    rammus.dot(20, random.choice(colourList))
    rammus.forward(50)
    if dotCount % 10 == 0:
        rammus.setheading(90)
        rammus.forward(50)
        rammus.setheading(180)
        rammus.forward(500)
        rammus.setheading(0)

screen = turtleModule.Screen()
screen.exitonclick()