import turtle
import random

screen = turtle.Screen()
screen.colormode(255)


# draw the boundary box
boxDrawer = turtle.Turtle()
boxDrawer.speed(10)
boxDrawer.color("red")
boxDrawer.penup()
boxDrawer.goto(-200, 200)
boxDrawer.pendown()
for i in range(4):
  boxDrawer.forward(400)
  boxDrawer.right(90)
boxDrawer.penup()

# create functions for keyboard events
def left():
  turtle.left(10)

def right():
  turtle.right(10)
  
# bind keyboard events to screen
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

# write score
score = 0
scoreTurtle = turtle.Turtle()
scoreTurtle.speed(750)
scoreTurtle.penup()
scoreTurtle.goto(-200,210)
scoreTurtle.write("Score: " + str(score))

# main loop - turtle continuously moves and checks if out of bounds
turtle.color("black")
turtle.goto(0,0)
turtle.pendown()
while True:
  turtle.forward(5)
  if turtle.xcor() > 200 or turtle.xcor() < -200:
    turtle.write("Out of bounds!")
    break
  elif turtle.ycor() > 200 or turtle.ycor() < -200:
    turtle.write("Out of bounds!")
    break
  else:
    # update score
    score += 1
    scoreTurtle.clear()
    scoreTurtle.write("Score: " + str(score))

screen.exitonclick()


