from state import State
class Policy():
    def __init__(self, state_keys, default_jump, default_stay):
        self.keys = state_keys
        self.d_jump = default_jump
        self.d_stay = default_stay
        self.states = self.initialize()

    def initialize(self):
        temp = {}
        for key in self.keys:
            temp[key] = State(self.d_jump, self.d_stay)
        return temp