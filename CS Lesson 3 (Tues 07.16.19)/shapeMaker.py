import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

turtle = turtle.Turtle()
turtle.speed(10000)
turtle.penup()

def drawSquare():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turtle.color(r,g,b)
  
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  turtle.goto(x,y)
  
  sideLength = random.randint(20,100)
  
  turtle.pendown()
  turtle.begin_fill()
  for i in range(4):
    turtle.forward(sideLength)
    turtle.right(90)
  turtle.end_fill()
  turtle.penup()

def drawOctagon():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turtle.color(r,g,b)
  
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  turtle.goto(x,y)
  
  sideLength = random.randint(20,100)
  
  turtle.pendown()
  turtle.begin_fill()
  for i in range(8):
    turtle.forward(sideLength)
    turtle.right(315)
  turtle.end_fill()
  turtle.penup()

def drawFirework():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turtle.color(r,g,b)
  
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  
  for i in range(36):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(20)
    turtle.right(10)
    turtle.penup()
  
def drawCircle():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  turtle.color(r,g,b)
  
  x = random.randint(-300,300)
  y = random.randint(-300,300)
  turtle.goto(x,y)
  
  sideLength = random.randint(5,20)
  
  turtle.pendown()
  turtle.begin_fill()
  for i in range(36):
    turtle.forward(sideLength)
    turtle.right(10)
  turtle.end_fill()
  turtle.penup()

screen.onkey(drawSquare, "Up")
screen.onkey(drawOctagon, "Down")
screen.onkey(drawFirework, "Left")
screen.onkey(drawCircle, "Right")
screen.listen()
screen.exitonclick()

