#!python3
from Game.Modules import *


class Score(Game_Object):
    def __init__(self):
        self.x = 50
        self.y = Constants.WINDOW_HEIGHT - 15
        self.value = 0
        self.sprite = Text(Point(self.x, self.y), f'Time: {self.value}')

    def start(self):
        self.start_time = time.time()
    
    def update(self):
        try:
            self.value = int((time.time() - self.start_time) * 1000)
        except AttributeError:
            print('!!! ERROR !!!: score.start() was never called.')
            raise
    
    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        self.sprite.setText(f'Time: {self.value}')
    
    def reset(self):
        self.start_time = time.time()

class High_Score(Game_Object):
    def __init__(self):
        self.x = Constants.WINDOW_WIDTH - 75
        self.y = Constants.WINDOW_HEIGHT - 15
        self.value = 0
        self.sprite = Text(Point(self.x, self.y), f'High Score: {self.value}')
    
    def update(self, x):
        if (x > self.value):
            self.value = x
    def draw(self, win):
        self.sprite.draw(win)
    
    def update_draw(self):
        self.sprite.setText(f'High Score: {self.value}')
        
    def reset(self):
        pass