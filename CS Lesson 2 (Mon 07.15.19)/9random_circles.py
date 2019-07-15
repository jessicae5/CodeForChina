import turtle
import random

screen = turtle.Screen()
screen.colormode(255)
turtle = turtle.Turtle()
turtle.speed(100000)

# set random number of squares
numSquares = 30

for i in range(numSquares):

	# set random color
	r = random.randint(0,256)
	g = random.randint(0,256)
	b = random.randint(0,256)
	turtle.color(r,g,b)

	# set random side length
	sideLength = random.randint(0, 200)

	# set random starting position
	x = random.randint(-300,300)
	y = random.randint(-300,300)
	turtle.penup()
	turtle.goto(x,y)

	# draw square
	turtle.pendown()
	turtle.begin_fill()

	angle = 10
	length = 5
	for i in range(36):
		turtle.forward(length)
		turtle.right(angle)
	turtle.end_fill()

	turtle.penup()
screen.exitonclick()