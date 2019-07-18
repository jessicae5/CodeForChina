# Globals
 
import pygame
import constants
import random 
 
 
 
"""
Paddle: A class to represent the paddle
"""
 
class Paddle(object):
 
    def __init__(self):
        self.x = (constants.SCREEN_WIDTH - constants.PADDLE_WIDTH) / 2
        self.y = constants.SCREEN_HEIGHT - constants.GAP - constants.PADDLE_HEIGHT
        self.width = constants.PADDLE_WIDTH
        self.height = constants.PADDLE_HEIGHT
        self.x_velocity = 0
        self.color = constants.PADDLE_COLOR
 
"""
Ball: A class to represent the ball
"""
class Ball(object):
 
    def __init__(self):
        self.radius = constants.BALL_RADIUS
        velocity_list = [10, -10]
        self.x_velocity = random.choice(velocity_list)
        self.y_velocity = 10
        self.x = constants.SCREEN_WIDTH / 2
        self.y = constants.SCREEN_HEIGHT / 2
        self.color = constants.BALL_COLOR;
 
 
"""
Brick: A class to represent the brick
"""
class Brick(object):
 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = constants.BRICK_WIDTH
        self.height = constants.BRICK_HEIGHT
        self.color = constants.BRICK_COLOR
 
 
def create_new_ball():
    return Ball()
 
def create_new_paddle():
    return Paddle()
 
def create_new_brick():
    return Brick()
 
# Get Methods 
 
def get_x(self):
    return self.x
 
def get_y(self):
    return self.y
 
def get_width(self):
    return self.width
 
def get_height(self):
    return self.height
 
def get_x_velocity(self):
    return self.x_velocity
 
def get_y_velocity(self):
    return self.y_velocity 
 
def get_radius(self):
    return self.radius 
 
 
def get_color(self):
    return self.color 
 
# Set Methods 
 
def set_x(self, x):
    self.x = x
 
def set_y(self, y):
    self.y = y
 
def set_width(self, w):
    self.width = w
 
def set_height(self, h):
    self.height = h
 
def set_x_velocity(self, v):
    self.x_velocity = v
 
def set_y_velocity(self, v):
    self.y_velocity = v
 
def set_radius(self, r):
    self.radius = r
 
def set_color(self, c):
    self.color = c
 
def clamp(n, min_n, max_n):
    return max(min(max_n, n), min_n)
 
def draw_rectangle(x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
 
def draw_circle(x, y, radius, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), radius)
 
def get_mouse_location():
    return pygame.mouse.get_pos();
 
 
# This function creates the window for the game. It should be called at
# the beginning of your program.
def build_screen(width, height):
    pygame.init()
    global screen
    screen = pygame.display.set_mode((width, height))
 
 
# This function wipes the screen clean by filling it with a color.
# This lets you draw new objects, or make objects look like they've moved.
def clear_screen():
    screen.fill(constants.SCREEN_COLOR)
 
# Check and see if the ball and another obj collided with each other 
def ball_did_collide_with(ball, obj, width, height):
    dist = 1.41*get_radius(ball)
    if (int(get_x(ball) - dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) - dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) + dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) - dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) + dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) + dist) in range(get_y(obj), get_y(obj) + height)) \
    or (int(get_x(ball) - dist) in range(get_x(obj), get_x(obj) + width) and int(get_y(ball) + dist) in range(get_y(obj), get_y(obj) + height)): 
        return True
    return False