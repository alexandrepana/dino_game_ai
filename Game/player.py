#!python3
from Game import Constants
from Game.graphics import *

# Our Player Class
class Player:
    def __init__(self):
        self.x = 50
        self.y = Constants.GROUND
        self.y_vel = 0
        self.jump_speed = 20
        self.gravity = 2.3
        self.grounded = 1
        self.height = 15
        self.width = 10
        self.sprite = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        self.sprite.setFill('green')

    def update(self, obstacle_manager):
        self.y += self.y_vel

        if (self.y <= Constants.GROUND):
            self.y = Constants.GROUND
            self.y_vel = 0
            self.grounded = 1
        else:
            self.y_vel -= self.gravity
            self.grounded = 0
        
        self.check_collisions(obstacle_manager)

    def jump(self):
        self.y_vel = self.jump_speed
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        # These are specifically for rectangles
        old_corner1 = self.sprite.getP1()
        # old_corner2 = self.sprite.getP2()
        self.sprite.move(self.x - old_corner1.getX(), self.y - old_corner1.getY())
    
    def check_collisions(self, obstacle_manager):
        for obstacle in obstacle_manager.obstacles:
            if (self.x + self.width > obstacle.x and
                self.x < obstacle.x + obstacle.width and
                self.y + self.height > obstacle.y and
                self.y < obstacle.y + obstacle.height):
                self.sprite.setFill('red')
    
    def reset(self):
        self.sprite.setFill('green')
