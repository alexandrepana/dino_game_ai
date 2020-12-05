#!python3
import itertools
from Game.Modules import *

class Sarsa():
    def __init__(self, epsilon, gamma, alpha, default_jump, default_stay):
        self.d_jump = default_jump
        self.d_stay = default_stay
        self.epsilon = epsilon
        self.gamma = gamma
        self.alpha = alpha
        self.policy = self.initialize_policy()

    def initialize_policy(self):
        l = [False, True]
        keys = list(itertools.product(l, repeat=Constants.UNIT_SIZE)) # How many segments exist
        keys = remove_unused(keys, Constants.NUM_OBSTACLES)

        temp = {}
        for key in keys:
            temp[key] = [self.d_jump, self.d_stay]
        return temp

    def give_policy(self, agent):
        self.policy = agent
        
    def select_action(self, key):
        x = random.random() # create random float between 0 - 1

        if (x > self.epsilon):
            choice = self.policy[key].index((random.choice(self.policy[key])))
        else:
            choice = self.policy[key].index((max(self.policy[key])))

        if(choice == 0): 
            return ("jump", 0)
        else:
            return (None, 1)

    def update_policy(self, key1, index1, key2, index2, reward):
        predict = self.policy[key1][index1]
        target = reward + self.gamma * self.policy[key2][index2]
        self.policy[key1][index1] += self.alpha * (target - predict)

    def test(self):
        print(closest_unit(750))

    def get_state(self, obstacles):
        new_state = [False for i in range(Constants.UNIT_SIZE)]
        for obj in obstacles:
            if(obj.x < Constants.WINDOW_WIDTH):
                new_state[closest_unit(obj.x)] = True
        return tuple(new_state)

def remove_unused(keys, max_num):
    temp = keys
    for key in keys:
        count = 0
        for val in key:
            if(val): count+=1
            if(count > 3):
                temp.remove(key)
                break
    return(temp)

def closest_unit(num):
    temp = float('%.1f'%(num/Constants.WINDOW_WIDTH))
    if(temp == 1): temp = 0.9
    index_finder = [ float('%.1f'%(i*(1/Constants.UNIT_SIZE))) for i in range(Constants.UNIT_SIZE)] # convert to string to remove floating point errors
    index = index_finder.index(temp)
    return index