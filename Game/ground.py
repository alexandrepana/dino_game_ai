#!python3
from Game.Modules import *


class Ground(Game_Object):
    def __init__(self):
        self.x1 = 0
        self.y1 = Constants.GROUND
        self.x2 = Constants.WINDOW_WIDTH
        self.y2 = Constants.GROUND
        self.sprite = Line(Point(self.x1, self.y1), Point(self.x2, self.y2))
        self.sprite.setFill('grey')
    
    def draw(self, win):
        self.sprite.draw(win)

    def update(self):
        pass
    
    def update_draw(self):
        pass
    
    def reset(self):
        pass