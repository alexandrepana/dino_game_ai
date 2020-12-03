#!python3
from AI.policy import *


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

    # gets the next state object, given the current state object and an action
    def getNextState(self, state, action):
        # action: 0 --- jump
        # action: 1 --- continue
        # should be the amount the distance between the player and the block changes each iteration
        distanceIncrement = 25
        # TODO: make sure this distance increment is correrct
        newDistance = min((distanceIncrement + state.distance), 0)

        # TODO: make sure this onGround increment is correct
        if (not state.onGround):  # currently in the air
            # TODO: if the player is within some threshold of the ground, onGround will be true in the next state
            if (action == 0):
                state.onGround = False
            elif (action == 1):
                pass
        else:  # currently not in the air
            if (action == 0):
                onGround = True    # player has chosen to jump
            elif (action == 1):
                pass            # player has chosen to continue

        # return the state with the incremeted distance, and the updated onGround, based on the action
        return self.getState(newDistance, state.onGround)


class State:
    def __init__(self, distance=0, onGround=True):
        self.policy = Policy()        # [0] = do nothing, [1] = jump
        self.distance = distance
        self.onGround = onGround
        self.reward = 1
