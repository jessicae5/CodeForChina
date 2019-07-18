#Complete this script first, then move your code into ballPaddle_Starter.py

#Import Statements
import turtle
import random
import time
import sys

#Global Variables
screen = turtle.Screen()
screen.screensize(400,400)
globalScreenSize = screen.screensize()
globalWidth = globalScreenSize[0]
globalHeight = globalScreenSize[1]
globalBallHeight = 10.0
screen.colormode(255)

screen.title("C4C Y1A Breakout")
ballTurtle = turtle.Turtle()
gameSpeed = 1

#Method that returns the location of the left side of the ball as a float
def leftOfBall():
  #Your code here.

#Method that returns the location of the right side of the ball as a float
def rightOfBall():
  #Your code here.

#Method that returns the location of the top side of the ball as a float
def topOfBall():
  #Your code here.

#Method that returns the location of the bottom side of the ball as a float
def bottomOfBall():
  #Your code here.

#Method that draws a border around the screen. Does not return anything
def drawOuterBox():
  #Your code here.

#Method that draws the ball to the screen. Does not return anything
def drawBall():
  #Your code here

#Method that returns the location of the left side of the wall as a float.
#Hint: Use globalWidth or globalHeight.
def leftOfWall():
  #Your code here

#Method that returns the location of the right side of the wall as a float.
def rightOfWall():
  #Your code here

#Method that returns the location of the top side of the wall as a float.
def topOfWall():
  #Your code here

#Method that returns the location of the bottom side of the wall as a float.
def bottomOfWall():
  #Your code here

#Method that moves the ballTurtle at the gameSpeed
def moveBall():
  #Your code here

#Method that checks the collisions between the ball and the wall. Does not return anything
#Hint #1: use the methods you wrote like leftOfBall() and leftOfWall()
def checkBallWallCollision():
  #Your code here

#Main Function
def main():
  screen.tracer(0, 0)
  drawOuterBox()
  drawBall()
  while True:
    checkBallWallCollision()
    moveBall()
    screen.update()
  turtle.done()
  turtle.exit()
  return 0

if __name__ == "__main__":
     main()
