import turtle
import random


screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(100)
turtle.pensize(5)

length = 10
for i in range(20):
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(100,255)
  turtle.color(r,g,b)

  turtle.forward(length)
  turtle.left(90)
  length = length + 10

screen.exitonclick()