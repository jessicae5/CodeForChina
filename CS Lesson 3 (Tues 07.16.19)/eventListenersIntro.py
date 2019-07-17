import turtle

screen = turtle.Screen()
screen.bgcolor("white")
turtle = turtle.Turtle()


def up():
    turtle.forward(100)

screen.onkey(up, "Up")
screen.listen()

screen.exitonclick()