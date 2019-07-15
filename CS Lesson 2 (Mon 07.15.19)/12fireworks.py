import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(1000)

lineLength = 1

for i in range(360):
  # set random color
  r = random.randint(0,256)
  g = random.randint(0,256)
  b = random.randint(0,256)
  turtle.color(r,g,b)
  
  # draw line
  turtle.goto(0,0)
  turtle.forward(lineLength)
  turtle.right(5)
  
  # increase length of line
  lineLength = lineLength + 1

screen.exitonclick()