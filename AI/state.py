#!python3
from policy import *


class State:
    def __init__(self):
        self.policy = Policy()        # [0] = do nothing, [1] = jump
        self.distances = []
        self.onGround = True
