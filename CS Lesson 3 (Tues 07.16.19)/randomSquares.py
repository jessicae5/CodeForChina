

import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
jess = turtle.Turtle()
jess.speed(0)

def drawSquare(sideLength, x, y):
    jess.penup()
    jess.goto(x, y)
    jess.pendown()
    for i in range(4): 
        jess.forward(sideLength)
        jess.left(90)

def getValue(low, high):
    value = random.randint(low, high)
    return value

def main():

    #### CODE HERE ####
    numSquares = 50
    for i in range(numSquares):
        sideLength = getValue(10, 100)
        x = getValue(-100, 100)
        y = getValue(-100, 100)
        drawSquare(sideLength, x, y)

    screen.exitonclick()

if __name__ == "__main__":
    main()