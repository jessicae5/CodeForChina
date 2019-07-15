import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(2)

for i in range(4):
  r = random.randint(0,256)
  g = random.randint(0,256)
  b = random.randint(0,256)
  turtle.color(r,g,b)
  
  length = 20
  
  for j in range(3):
    length = length + 20
    
    for j in range(4):
      turtle.forward(length)
      turtle.right(90)
  
  turtle.right(90)
screen.exitonclick()