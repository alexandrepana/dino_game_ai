#!python3
from graphics import *

# Constants
GROUND = 100

# Our Player Class
class Obstacle:
    def __init__(self, max_x):
        self.x = max_x
        self.y = GROUND
        self.height = 20
        self.width = 20
        self.speed = 16
        self.max_x = max_x
        self.sprite = 'to do'

    def update(self):
        self.x -= self.speed

        # Check if Obstacle is off-screen
        if (self.x <= -self.width):
            self.x = self.max_x
    
    def draw(self, win):
        rect = Rectangle(Point(self.x, win.height - self.y), Point(self.x + self.height, win.height - self.y - self.width))
        rect.setFill('red')
        rect.draw(win)