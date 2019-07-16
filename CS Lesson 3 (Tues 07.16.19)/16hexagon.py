import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(10)

for i in range(6):
  r = random.randint(0,256)
  g = random.randint(0,256)
  b = random.randint(0,256)
  turtle.color(r,g,b)
  
  length = 30
  
  for j in range(3):
    length += 15
    
    for j in range(6):
      turtle.forward(length)
      turtle.right(120)
  
  turtle.right(60)

screen.exitonclick()