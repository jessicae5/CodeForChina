import turtle
import random

# draw starting lines
laneDrawer = turtle.Turtle()
laneDrawer.right(90)
laneDrawer.speed(1000)
laneDrawer.penup()
laneDrawer.goto(-200, 100)
num = 1
for i in range(16):
  laneDrawer.write(num)
  laneDrawer.pendown()
  laneDrawer.forward(100)
  laneDrawer.backward(100)
  laneDrawer.penup()
  laneDrawer.left(90)
  laneDrawer.forward(20)
  laneDrawer.right(90)
  num = num + 1
  

laneDrawer.ht()

# set up the race turtles
t1 = turtle.Turtle()
t1.penup()
t1.color("red")
t1.shape("turtle")
t1.goto(-200,90)
t1.pendown()

t2 = turtle.Turtle()
t2.penup()
t2.color("blue")
t2.shape("turtle")
t2.goto(-200,50)
t2.pendown()

t3 = turtle.Turtle()
t3.penup()
t3.color("orange")
t3.shape("turtle")
t3.goto(-200,10)
t3.pendown()

# race the turtles
for i in range(29):
  t1.forward(random.randint(5,20))
  t2.forward(random.randint(5,20))
  t3.forward(random.randint(5,20))

# check who won or tied
if t1.xcor() > t2.xcor() and t1.xcor() > t3.xcor():
  t1.write("I win!", font=("Arial", 16, "normal"))
elif t2.xcor() > t1.xcor() and t2.xcor() > t3.xcor():
  t2.write("I win!", font=("Arial", 16, "normal"))
elif t3.xcor() > t1.xcor() and t3.xcor() > t2.xcor():
  t3.write("I win!", font=("Arial", 16, "normal"))
elif t1.xcor() == t2.xcor() and t2.xcor() == t3.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t2.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))
elif t1.xcor() == t2.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t2.write("Tie!", font=("Arial", 16, "normal"))
elif t1.xcor() == t3.xcor():
  t1.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))
elif t2.xcor() == t3.xcor():
  t2.write("Tie!", font=("Arial", 16, "normal"))
  t3.write("Tie!", font=("Arial", 16, "normal"))

  screen.exitonclick()