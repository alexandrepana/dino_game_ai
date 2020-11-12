#!python3
import Constants
from graphics import *

# Our Player Class
class Obstacle:
    def __init__(self):
        self.x = Constants.WINDOW_WIDTH
        self.y = Constants.GROUND
        self.height = 20
        self.width = 20
        self.speed = 16
        self.sprite = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))

    def update(self):
        self.x -= self.speed

        # Check if Obstacle is off-screen
        if (self.x <= -self.width):
            self.x = Constants.WINDOW_WIDTH
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        # These are specifically for rectangles
        old_corner1 = self.sprite.getP1()
        # old_corner2 = self.sprite.getP2()
        self.sprite.move(self.x - old_corner1.getX(), self.y - old_corner1.getY())