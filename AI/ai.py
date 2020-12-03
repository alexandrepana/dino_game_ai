#!python3
import policy

class AI:
    def __init__(self):
        self.policy = Policy()        # [0] = do nothing, [1] = jump
        self.grid = []

    # self.player, self.obstacle_manager, self.score, self.ground
    def get_state(player, obstacle_manager, score, ground):
        #distance = player.x - obstacle_manager.obstacles[0]

        # list of distances to each object that is on the screen
        # dino is on the ground
