#!python3

class Policy:
    def __init__(self):
        self.jumpProb = 0.5
        self.continueProb = 0.5

    def getValues(self):
        return [self.jumpProb, self.continueProb]

    def update(self, action, newValue):
        if (action == 0):
            self.jumpProb = newValue
        elif (action == 1):
            self.continueProb = newValue
