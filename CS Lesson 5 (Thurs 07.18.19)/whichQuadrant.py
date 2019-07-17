#Import Statements
import turtle
import random

#Global Variables
screen = turtle.Screen()
jess = turtle.Turtle()
screen.colormode(255)
squareLength = 25

#Helper Functions

#DON'T TOUCH THIS
def drawLines():
  bob = turtle.Turtle()
  bob.speed(0)
  bob.goto(1000,0)
  bob.goto(-1000,0)
  bob.goto(0,0)
  bob.goto(0,1000)
  bob.goto(0,-1000)
  
#This function takes the parameters x,y which desribe the location
#of the user's click. Based on the coordinate the function
#returns the number 1,2,3 or 4 which is the quadrant that the
#click occured in.
def whichQuadrant(x,y):
  return

def locationToText(x,y):
  text = "(" + str(x) + ", " + str(y) + ")"
  return text

def clickedFunction(x, y):
  jess.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
  text = locationToText(x,y)
  jess.goto(x,y)
  jess.write(text)

#Main Function
def main():
  drawLines()
  jess.penup()
  screen.onclick(clickedFunction)
  screen.listen()
  turtle.done()
  return 0

if __name__ == "__main__":
  main()