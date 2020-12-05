import random
class Sarsa():
    def __init__(self, epsilon, state_keys, default_jump, default_stay):
        self.keys = state_keys
        self.d_jump = default_jump
        self.d_stay = default_stay
        self.epsilon = epsilon
        self.policy = self.initialize()

    def initialize(self):
        temp = {}
        for key in self.keys:
            temp[key] = [self.d_jump, self.d_stay]
        return temp

    def select(self, key):
        x = random.random() # create random float between 0 - 1
        if (x > self.epsilon):
            return random.choice(self.policy[key]).index
        else:
            return max(self.policy[key]).index