import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(100000)

# set random number of triangles
numTriangles = 30

for i in range(numTriangles):

  
  # set random color
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turtle.color(r,g,b)
  
  # set random side length
  sideLength = random.randint(0, 200)
  
  # set random starting position
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  turtle.penup()
  turtle.goto(x,y)
  
  # draw triangle
  turtle.pendown()
  turtle.begin_fill()
  angle = 120
  for i in range(3):
    turtle.forward(sideLength)
    turtle.right(120)
  turtle.end_fill()
  
  turtle.penup()
screen.exitonclick()