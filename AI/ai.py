#!python3

class AI:
    def __init__(self):
        self.policy = [0.2, 0.8]        # [0] = do nothing, [1] = jump
        self.grid = []