#!python3
from graphics import *

# Constants
GRAVITY = 1
GROUND = 100


# Our Player Class
class Player:
    def __init__(self):
        self.x = 50
        self.y = GROUND
        self.y_vel = 0
        self.jump_speed = 10
        self.grounded = 1
        self.height = 10
        self.width = 15
        self.sprite = 'to do'

    def update(self):
        self.y += self.y_vel

        if (self.y <= GROUND):
            self.y = GROUND
            self.y_vel = 0
            self.grounded = 1
        else:
            self.y_vel -= GRAVITY
            self.grounded = 0

    def jump(self):
        self.y_vel = self.jump_speed
    
    def draw(self, win):
        rect = Rectangle(Point(self.x, win.height - self.y), Point(self.x + self.height, win.height - self.y - self.width))
        rect.draw(win)