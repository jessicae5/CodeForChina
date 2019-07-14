import turtle
import random
screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(1)

length = random.randint(30, 250)
angle = 120
sides = 3

for i in range(sides):
  turtle.forward(length)
  turtle.left(angle)

screen.exitonclick()