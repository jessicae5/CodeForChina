import turtle

screen = turtle.Screen()
screen.colormode(255)

turtle = turtle.Turtle()

turtle.speed(1)

length = 10
turtle.right(60)
for i in range(25):
  turtle.penup()
  turtle.goto(0,200)
  turtle.pendown()
  
  for j in range(3):
    turtle.forward(length)
    turtle.right(120)
    
  length = length + 10
screen.exitonclick()