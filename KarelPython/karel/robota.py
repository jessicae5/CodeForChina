""" Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License

Defines the UrRobot and Robot classes and some associated infrastructure. 
UrRobots have no predicate methods, hence cannot query the world.
Robot objects extend UrRobots and have a variety of sensors for learning about their environment.
"""
import sys
import time
from copy import copy
#from exceptions import NotImplementedError
#from exceptions import Exception
from karel.observable import Observable


noGraphics = 0
tkGraphics = 2

graphics = tkGraphics

from karel.basicdefinitions import North 
from karel.basicdefinitions import West
from karel.basicdefinitions import South
from karel.basicdefinitions import East

from karel.basicdefinitions import infinity 
from karel.basicdefinitions import legalCorner
from karel.basicdefinitions import NoBeepers
from karel.basicdefinitions import IllegalCorner

if  graphics == noGraphics:
    from karel.robotworld import RobotWorld
    from karel.robotworld import window
    from karel.robotworld import world
elif graphics == tkGraphics :
    from karel.tkworldadapter import RobotWorld
    from karel.tkworldadapter import world
    from karel.tkworldadapter import window
else :
    print("No graphics system defined. Exiting")
    exit()
    

print()
print (world.name()) # printed when this module loads
print()

#_displayCharacter = { North: " ^ ", East: " > ", South: " v ", West: "<  " }
#_nextDirection = {North: West, West: South, South: East, East: North}
from karel.basicdefinitions import _nextDirection
__robotCount = -1

def _incrementRobotCount() :
    global __robotCount
    __robotCount += 1
    return __robotCount

from karel.basicdefinitions import NoBeepersInBeeperBag
from karel.basicdefinitions import RobotNotRunning
from karel.basicdefinitions import FrontIsBlocked            

class _RobotSkeleton:
    """ Defines the basic structure of a simple robot produced by the Karel Werke. This skeleton has no
    working parts. If you try to send a message to such a machine, it will simply signal an error. 
    """
    def move(self):
        "Move one block forware (standard version)"
        raise NotImplementedError("move not yet implemented.") 
    def turnLeft(self):
        "Turn 90 degrees to the left (standard version)"
        raise NotImplementedError("turnLeft not yet implemented.")
    def pickBeeper(self):
        "Pick one beeper from the current corner if present (standard version)"
        raise NotImplementedError("pickBeeper not yet implemented.") 
    def putBeeper(self):
        "Put one beeper on the current corner if holding any (standard version)"
        raise NotImplementedError( "putBeeper not yet implemented.")
    def turnOff(self):
        "Turn off and accept no further instructions (standard version)"
        raise NotImplementedError("turnOff not yet implemented.") 
    

class UrRobot(_RobotSkeleton, Observable):
    "The most primitive kind of robot. Has no sensing facilities. Knows how to interact with the world." 
    
    moveAction = 0 #These are nominal values only
    turnLeftAction = 1
    pickBeeperAction = 2
    putBeeperAction = 3
    turnOffAction = 4
    createAction = 5
    
    def __init__(self, street, avenue, direction, beepers, fill = 'blue', outline = 'black'):
        "Create a robot in a particular situation."
        Observable.__init__(self)
        legalCorner(street, avenue)
        self.__street = street
        self.__avenue = avenue
        self.__direction = direction
        if beepers < 0 :
            beepers = infinity
        self.__beepers = beepers
        self.__fill = fill
        self.__outline = outline
        self.__running = True;
        self.addObserver(world)
#        world._World__registerRobot(self)
        self.setChanged()
        self.notifyObservers(self.RobotState(self, self.createAction))
        self.__pausing = False
        self.__userPausing = False
        self.__ID = _incrementRobotCount()
        
    def clone(self):
        robot = copy(self)
        robot.__ID = _incrementRobotCount()
        Observable.__init__(robot)
        robot.addObserver(world)
        robot.setChanged()
        robot.notifyObservers(robot.RobotState(robot, robot.createAction))
        return robot

    def display(self):
        "Print out the current situation of the robot."
        print ("Robot with ID: " + str(self.__ID))
        print ("Street " + str(self.__street))
        print ("Avenue " + str(self.__avenue))
        print ("Direction " + self.__direction.__name__)
        beepers = self.__beepers
        if beepers >= 0 :
            print ("Beepers " + str(beepers))
        else :
            print ("Beepers infinity" )
        if self.__running :
            print ("Running")
        else:
            print ("Not running")
            
    def showState(self, message):
        print (message)
        self.display()
            
    def ID(self):
        return self.__ID
    
    def isRunning(self):
        return self.__running
              
    def move(self):
        "Move one block in the current direction or fail if the front is not clear."
        self.__pause('move')
        if not self.__running :
            raise RobotNotRunning("Cannot move.")
        self.__speedCheck()
        self.__direction(self, world)
#        world._World__registerRobot(self)
        self.setChanged()
        self.notifyObservers(self.RobotState(self, self.moveAction))
        self.sleep()

    def __speedCheck(self):
        world.speedCheck()
            
    def turnOff(self):
        "Turn the robot off. After turnOff the robot will give errors if sent other messages."
        self.__pause('turnOff')
        self.__speedCheck()
        self.__running = False;
        self.setChanged()
        self.notifyObservers(self.RobotState(self, self.turnOffAction))
        self.sleep()

    def turnLeft(self):
        "Turn ninety degrees to the left."
        self.__pause('turnLeft')
#        directions = (north, west, south, east)
        if not self.__running :
            raise RobotNotRunning( "Cannot turnLeft.")
        self.__speedCheck()
        self.__direction = _nextDirection[self.__direction]
        self.setChanged()
        self.notifyObservers(self.RobotState(self, self.turnLeftAction))
        self.sleep()

    def pickBeeper(self):
        "Pick a beeper from the current corner or fail if there are none to pick."
        self.__pause('pickBeeper')
        if not self.__running :
            raise RobotNotRunning( "Cannot pickBeeper.")
        self.__speedCheck()
        try :
            world.removeBeeper(self.__street, self.__avenue, False)
            beepers = self.__beepers
            if beepers >= 0 :
                self.__beepers = beepers + 1
            self.setChanged()
            self.notifyObservers(self.RobotState(self, self.pickBeeperAction))
        except NoBeepers as data : 
            self.turnOff()
            self.setChanged()
#            self.notifyObservers(self.RobotState(self, self.pickBeeperAction))
            print (str(data))
            raise Exception("Failed to Pick Beeper")
#            world.error(NoBeepers() + ": " +data)
        self.sleep()
        # more
        
    def putBeeper(self):
        "Place a beeper on the current corner or fail if none are carried."
        self.__pause('putBeeper')
        if not self.__running :
            raise RobotNotRunning( "Cannot putBeeper.")
            #world.error("Robot not running. Cannot putBeeper.")
        self.__speedCheck()
        beepers = self.__beepers
        if  beepers > 0 :
            self.__beepers = beepers - 1
            world.placeBeepers(self.__street, self.__avenue, 1)
        elif beepers == infinity :
            world.placeBeepers(self.__street, self.__avenue, 1)
        else :
            self.turnOff()
            self.setChanged()
            self.notifyObservers(self.RobotState(self, self.putBeeperAction))
            raise NoBeepersInBeeperBag()
        self.setChanged()
        self.notifyObservers(self.RobotState(self, self.putBeeperAction))
        self.sleep()
        
    def sleep(self):
        if world.delay() > 0 :
            time.sleep(world.delay() / 100.0) # FIXME: Tune this delay
            
        # see RobotWorld.setDelay
        
    def run(self):
        pass
        
    def __pause(self, action):
        if not self.__pausing : return
        print ('Robot with ID: ' + str(self.__ID) + ' is about to ' + action +'.')
        sys.stdin.read(1)
        
    def userPause(self, action):
        if not self.__userPausing : return
        print ('Robot with ID: ' + str(self.__ID) + ' is about to ' + action +'.')
        sys.stdin.read(1)
    
    def setPausing(self, bool):
        self.__pausing = bool
        
    def setUserPausing(self, bool):
        self.__userPausing = bool
        
    def neighbors(self):
        "Return a list of the other robots on the current corner." 
        return world._neighborsOf(self)
    
    class RobotState:
        "Snapshots the state of a robot for graphics, tracing, ..."
        def __init__(self, robot, action):
            self.__street = robot._UrRobot__street
            self.__avenue = robot._UrRobot__avenue
            self.__direction = robot._UrRobot__direction
            self.__beepers = robot._UrRobot__beepers
            self.__running = robot._UrRobot__running
            self.__action = action
        def street(self):
            return self.__street
        def avenue(self):
            return self.__avenue
        def direction(self):
            return self.__direction
        def beepers(self):
            return self.__beepers
        def isRunning(self):
            return self.__running
        def action(self):
            return self.__action
        
from karel.sensorpack import _SensorPack
    
class Robot(UrRobot, _SensorPack) :
    "Adds sensing facilities to robots, but otherwise these behave just like UrRobots."
    
    def __init__(self, street, avenue, direction, beepers, fill = 'blue', outline = 'black'):
        UrRobot.__init__(self, street, avenue, direction, beepers, fill, outline )
        
    def anyBeepersInBeeperBag(self):
        "Return true if there are beepers carried by this robot."
        return self._UrRobot__beepers != 0    
    
    def nextToABeeper(self):
        "Return true if there are beepers on the current corner."
        return world._beepersAt(self._UrRobot__street, self._UrRobot__avenue)
    
    def facingNorth(self):
        "Return true if this robot is facing north."
        return self._UrRobot__direction == North
    
    def facingEast(self):
        "Return true if this robot is facing east."
        return self._UrRobot__direction == East
    
    def facingSouth(self):
        "Return true if this robot is facing south."
        return self._UrRobot__direction == South
    
    def facingWest(self):
        "Return true if this robot is facing west."
        return self._UrRobot__direction == West
    
    def frontIsClear(self):
        "Return true if there is no wall immediately in front of this robot."
        return world._clearBefore(self)
    
    def nextToARobot(self):
        "Return true if there are any other robots on the current corner."
        return self.neighbors() != []