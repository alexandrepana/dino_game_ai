#!python3
import Constants
from graphics import *

# Our Player Class
class Player:
    def __init__(self):
        self.x = 50
        self.y = Constants.GROUND
        self.y_vel = 0
        self.jump_speed = 10
        self.grounded = 1
        self.height = 15
        self.width = 10
        self.sprite = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))

    def update(self):
        self.y += self.y_vel

        if (self.y <= Constants.GROUND):
            self.y = Constants.GROUND
            self.y_vel = 0
            self.grounded = 1
        else:
            self.y_vel -= Constants.GRAVITY
            self.grounded = 0

    def jump(self):
        self.y_vel = self.jump_speed
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        # These are specifically for rectangles
        old_corner1 = self.sprite.getP1()
        # old_corner2 = self.sprite.getP2()
        self.sprite.move(self.x - old_corner1.getX(), self.y - old_corner1.getY())