#!python3
from Game.Modules import *

class Game_Object_Holder:
    def __init__(self):
        self.player = Player()
        self.obstacle_manager = Obstacle_Manager()
        self.score = Score()
        self.ground = Ground()
    
    # Don't even ask about this...
    def function(self, function, window):
        exec(f'self.player.{function}({window})')
        exec(f'self.obstacle_manager.{function}({window})')
        exec(f'self.score.{function}({window})')
        exec(f'self.ground.{function}({window})')
