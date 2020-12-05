#!python3
import Constants
from obstacle import Obstacle
import random
import itertools

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
            choice = random.choice(self.policy[key]).index
        else:
            choice = max(self.policy[key]).index

        if(choice == 0): 
            return ("jump", 0)
        else:
            return (None, 1)

    def update(self, key1, index1, key2, index2, reward):
        predict = self.policy[key1][index1]
        target = reward + gamma * self.policy[key2][index2]
        self.policy[key1][index1] += alpha * (target - predict)

    # def get_state(self, obstacles):
    #     for obj in obstacles:


    
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
    new_state = [False for i in range(Constants.UNIT_SIZE)]
    print(new_state)
    index_finder = [i*(1/Constants.UNIT_SIZE) for i in range(UNIT_SIZE)]
    print(index_finder)
    return new_state

closest_unit(25)