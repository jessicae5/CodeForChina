#Import Statements
import turtle
import random

#Global Variables
screen = turtle.Screen()
screen.colormode(255)
turtles = []

#TODO: append to the global list turtles append the number of
#turtles given by the parameter numberTurtles
def makeTurtles(numberTurtles):


def moveTurtles():
  for turtle in turtles:
      turtle.speed(3)
      turtle.left(random.randint(0,360))
      turtle.color(random.randint(0,256),random.randint(0,256),random.randint(0,256))
      turtle.forward(200)

#Main Function
def main():
     #####Code Goes HERE#####
  makeTurtles(10)
  moveTurtles()
   ########################
  screen.exitonclick()
  return 0

if __name__ == "__main__":
     main()
