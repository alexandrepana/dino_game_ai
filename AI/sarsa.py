import random
class Sarsa():
    def __init__(self, epsilon, gamma, alpha, state_keys, default_jump, default_stay):
        self.keys = state_keys
        self.d_jump = default_jump
        self.d_stay = default_stay
        self.epsilon = epsilon
        self.gamma = gamma
        self.alpha = alpha
        self.policy = self.initialize()

    def initialize(self):
        temp = {}
        for key in self.keys:
            temp[key] = [False, self.d_jump, self.d_stay]
        return temp

    def select(self, key):
        x = random.random() # create random float between 0 - 1
        if (x > self.epsilon):
            return random.choice(self.policy[key]).index
        else:
            return max(self.policy[key]).index

    def update(self, keys1, index, keys2, index2, reward):
        
        for key1 in keys1:
            for key2
            predict = self.policy[key][index]
            target = reward + gamma * self.policy[key2][index2]
            self.policy[key1][index] += alpha * (target - predict)