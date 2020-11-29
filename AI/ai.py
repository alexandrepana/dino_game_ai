#!python3
from AI.Modules import *

class AI:
    def __init__(self):
        self.policy = Policy()        # [0] = do nothing, [1] = jump
        self.grid = []