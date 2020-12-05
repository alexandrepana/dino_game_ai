class State():
    def __init__(self, jump, stay):
        self.jump = jump
        self.stay = stay
    
    def update(self, jump, stay):
        self.jump = jump
        self.stay = stay