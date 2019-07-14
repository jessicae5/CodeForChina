import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(1000)

angle = 123

for i in range(100):

  r = random.randint(0,256)
  g = random.randint(0,256)
  b = random.randint(0,256)
  turtle.color(r,g,b)
  
  x = random.randint(-200,200)
  y = random.randint(-200,200)
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  
  length = random.randint(25,150)
  
  for i in range(50):
    turtle.forward(length)
    turtle.left(angle)
  
screen.exitonclick()