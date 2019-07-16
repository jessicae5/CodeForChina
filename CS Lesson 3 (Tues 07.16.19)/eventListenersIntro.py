import turtle

screen = turtle.Screen()
screen.bgcolor("white")
turtle = turtle.Turtle()


def up():
    turtle.forward(100)

def down():
    turtle.left(90)
    turtle.forward(100)

def left():
    turtle.left(90)
    turtle.forward(100)

def right():
    turtle.left(90)
    turtle.forward(100)

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(right, "Right")
screen.onkey(left, "Left")

screen.listen()

screen.exitonclick()