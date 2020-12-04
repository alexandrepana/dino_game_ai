#!python3
from AI.policy import *
from Game.Modules import *


class States:
    def __init__(self, distances):
        self.tStates = {}
        self.fStates = {}
        # Should we have this stored here? like call getState with the distance and it will return the state we want?

        # NOTE: KEY = str(distance)

        for i in range(len(distances)):
            key = str(distances[i])

            self.tStates[key] = State(distances[i], True)
            self.fStates[key] = State(distances[i], False)

    # gets the current state object (S)
    def getState(self, distance, onGround):
        key = str(distance)

        if not (key in self.tStates.keys()):
            self.tStates[key] = State(distance, True)
        if not (key in self.fStates.keys()):
            self.fStates[key] = State(distance, False)

        if onGround:
            return self.tStates[key]
        else:
            return self.fStates[key]


class State:
    def __init__(self, distance=0, onGround=True):
        self.policy = Policy()        # [0] = do nothing, [1] = jump
        self.distance = distance
        self.onGround = onGround
