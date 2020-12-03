#!python3

class Policy:
    def __init__(self):
        self.jumpProb = 0.5
        self.continueProb = 0.5

    def getValues(self):
        return (self.jumpProb, self.continueProb)
