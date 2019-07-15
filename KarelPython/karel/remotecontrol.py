'''Copyright 2008 Joseph Bergin
License: Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License

This is just a sample. The RemoteControl of kareltherobot accepts the usual 
parameters of UrRobots. You can also read a world here if you like, of course. 
Works only in Jython. Requires the kareltherobot.jar fils.
'''

from sys import argv

from kareltherobot import RemoteControl
from kareltherobot.Directions import East
from kareltherobot.Directions import infinity

from kareltherobot import World

class RemoteController:
    
    def show(self):
        World.setVisible(1)
        World.setDelay(0)
        builder = RemoteControl(1, 1, East, infinity)
        
    def setSize(self,streets, avenues):
        World.setSize(streets, avenues)
        
        
if __name__ == '__main__' :
    controller = RemoteController()
    controller.setSize(12, 12)
    if len(argv) > 1 :
        World.readWorld(argv[1])
    controller.show()