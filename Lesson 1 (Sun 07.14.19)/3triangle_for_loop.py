import turtle
screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(1)

length = 100
angle = 120
sides = 3

for i in range(3):
	turtle.forward(length)
	turtle.left(angle)

screen.exitonclick()