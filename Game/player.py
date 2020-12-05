#!python3
from Game.Modules import *


# Our Player Class
class Player(Game_Object):
    def __init__(self):
        self.x = Constants.SPAWN
        self.y = Constants.GROUND
        self.y_vel = 0
        self.jump_speed = 20
        self.gravity = 2.3
        self.grounded = 1
        self.height = 15
        self.width = 10
        self.sprite = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        self.sprite.setFill('green')

    def update(self):
        self.y += self.y_vel

        if (self.y <= Constants.GROUND):
            self.y = Constants.GROUND
            self.y_vel = 0
            self.grounded = 1
        else:
            self.y_vel -= self.gravity
            self.grounded = 0

    def jump(self):
        self.y_vel = self.jump_speed
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        old_corner1 = self.sprite.getP1()
        self.sprite.move(self.x - old_corner1.getX(), self.y - old_corner1.getY())
    
    def change_colour(self, colour=None):
        if (not colour):
            colour = [random.randrange(0, 100), random.randrange(200, 255), random.randrange(50, 150)]
        self.sprite.setFill(color_rgb(colour[0], colour[1], colour[2]))
    
    def reset(self):
        self.sprite.setFill('green')
