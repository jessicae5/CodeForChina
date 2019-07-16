import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

turtle = turtle.Turtle()
turtle.speed(1000)

r = random.randint(0,256)
g = random.randint(0,256)
b = random.randint(0,256)
turtle.color(r,g,b)

for i in range(6):
  turtle.goto(0,0)
  
  for i in range(10):
    # draw part of the branch
    turtle.forward(10)
    
    # draw a little side branch
    turtle.right(45)
    turtle.forward(20)
    turtle.backward(20)
    
    # draw the symmetrical little side branch
    turtle.left(90)
    turtle.forward(20)
    turtle.backward(20)
    
    # reset positioning
    turtle.right(45)
  
  # turn to start drawing the next branch
  turtle.right(60)

screen.exitonclick()
    