#Complete this script second, then move your code into breakout_Starter.py

#Import Statements
import turtle
import random
import time
import sys

#Global Variables
globalScore = 0
scoreTurtle = turtle.Turtle()
globalStarted = False
screen = turtle.Screen()
screen.screensize(400,400)
globalScreenSize = screen.screensize()
globalWidth = globalScreenSize[0]
globalHeight = globalScreenSize[1]
globalBallHeight = 10.0
screen.colormode(255)

globalSideGapRatio = .025
globalWidthGap = globalWidth * globalSideGapRatio
globalHeightGap = globalWidthGap * 2.0
widthBrick = ((globalWidth - (2*globalWidthGap))/10.0)
heightBrick = 20

screen.title("C4C Y1A Breakout")
blocks = []
numBricksRow = 10
numRows = 4
ballTurtle = turtle.Turtle()
gameSpeed = 5
paddleWidth = 40
paddleHeight = 10
paddleTurtle = turtle.Turtle()

#Helper Functions
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

#Method that returns the location of the left side of the paddle as a float
def leftOfPaddle():
  #Your code here.

#Method that returns the location of the right side of the paddle as a float
def rightOfPaddle():
  #Your code here.

#Method that returns the location of the top side of the paddle as a float
def topOfPaddle():
  #Your code here.

#Method that returns the location of the bottom side of the paddle as a float
def bottomOfPaddle():
  #Your code here.

#Method that returns the location of the X axis center of the paddle as a float
def centerOfPaddleX():
  #Your code here.

#Method that returns the location of the Y axis center of the paddle as a float
def centerOfPaddleY():
  #Your code here.

#Method that moves the ballTurtle at the gameSpeed
def moveBall():
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

#Method that draws a border around the screen. Does not return anything
def drawOuterBox():
  #Your code here.

#Method that draws the ball to the screen. Does not return anything
def drawBall():
  #Your code here

#Method that moves the paddleTurtle left.
def pressLeftKey():
  #Your code here.

#Method that moves the paddleTurtle right.
def pressRightKey():
  #Your Code Here

#Method that draws the paddle. Does not return anything
def drawPaddle():
  #Your code here

#Method that checks the collisions between the ball and the wall. Does not return anything
#Hint #1: use the methods you wrote like leftOfBall() and leftOfWall()
def checkBallWallCollision():
  #Your code here

#Method that checks the collisions between the paddle and the wall. Does not return anything
def checkPaddleWallCollision():
  #Your code here

#Method that checks the collisions between the paddle and the ball. Does not return anything
def checkPaddleBallCollision():
  #Your code here

#Main Function
def main():
  screen.onkey(pressLeftKey, "Left")
  screen.onkey(pressRightKey, "Right")
  screen.listen()
  screen.tracer(0, 0)
  drawOuterBox()
  drawBall()
  drawPaddle()
  while True:
    moveBall()
    checkBallWallCollision()
    checkPaddleBallCollision()
    checkPaddleWallCollision()
    screen.update()
  turtle.done()
  turtle.exit()
  return 0

if __name__ == "__main__":
     main()
