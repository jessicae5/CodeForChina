import turtle

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(100000)

angle = 10
length = 5
turtle.begin_fill()
for i in range(36):
  turtle.forward(length)
  turtle.right(angle)
turtle.end_fill()

screen.exitonclick()