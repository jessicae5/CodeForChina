from karel.robota import Robot
from karel.robota import East
from karel.robota import South
from karel.robota import North
from karel.robota import West
from karel.robota import window
from karel.robotworld import infinity
from karel.robota import world
import sys
from pathlib import Path

world_file = ""
if sys.argv[1].startswith("worlds"):
    path_split = sys.argv[1].split("/")
    worlds_folder = Path(path_split[0])
    world_file = worlds_folder / path_split[1]
else:
    world_file = sys.argv[1]

world.readWorld(world_file)
world.setVisible(True)
world.setDelay(50)

with open(world_file, 'r') as f:
    first_line = f.readline().strip()
configs = first_line.split("-")
direction = None
if configs[2].lower() == "east":
    direction = East
elif configs[2].lower() == "west":
    direction = West
elif configs[2].lower() == "north":
    direction = North
elif configs[2].lower() == "south":
    direction = South
num_beepers = 0
if configs[3].lower() == "inf":
    num_beepers = infinity
else:
    num_beepers = int(configs[3])

karel = Robot(int(configs[0]),int(configs[1]),direction,num_beepers)

move = karel.move
turn_left = karel.turnLeft
pick_beeper = karel.pickBeeper
put_beeper = karel.putBeeper
facing_north = karel.facingNorth
facing_south = karel.facingSouth
facing_east = karel.facingEast
facing_west = karel.facingWest
front_is_clear = karel.frontIsClear
on_beeper = karel.nextToABeeper


def right_is_clear():
    karel.turnLeft()
    karel.turnLeft()
    karel.turnLeft()
    val = karel.frontIsClear()
    karel.turnLeft()
    return val


def left_is_clear():
    karel.turnLeft()
    val = karel.frontIsClear()
    karel.turnLeft()
    karel.turnLeft()
    karel.turnLeft()
    return val

def execute_karel_task(task):
    window().setTask(task)
    window().setWorld(world)
    window().activate()
