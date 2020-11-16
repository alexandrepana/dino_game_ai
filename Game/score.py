#!python3
from Game import Constants
import time
from Game.graphics import *

class Score:
    def __init__(self):
        self.x = Constants.WINDOW_WIDTH - 100
        self.y = 25
        self.value = 0
        self.sprite = Text(Point(self.x, self.y), f'Time: {self.value}')

    def start(self):
        self.start_time = time.time()
    
    def update(self):
        try:
            self.value = int((time.time() - self.start_time) * 1000)
            # self.value = 0
        except AttributeError:
            print('!!! ERROR !!!: score.start() was never called.')
            raise
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        self.sprite.setText(f'Time: {self.value}')
    
    def reset(self):
        self.start_time = time.time()