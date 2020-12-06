'''
state space = [row, column]
    row = height of player (i.e. top row or bottom row)
    column = column of player (column of player in the state space)

policy = 3d array
    row = row of state
    column = column of state
    in each position ([jump, continue])
'''
cols = 50
rows = 2
bottomRow = rows-1
lastCol = cols-1
goal_state = (bottomRow, lastCol)
start_state = (1, 0)
episodes = 1

obstacle1 = (bottomRow, 10)
obstacle2 = (bottomRow, 40)


def eGreedy(stateSpace, state, e):
    i = state[0]
    j = state[1]

    actionArray = stateSpace[i][j]
    possibleActions = ["jump", "continue"]

    choice = choices(["max", "other"], weights=[1 - e + e /
                                                len(possibleActions), e/len(possibleActions)])[0]

    if choice == "max":
        return actionArray.index(max(actionArray))
    else:
        return actionArray.index(choices(actionArray))


def SARSA(a, e, learningRate):
    '''
        # Q-LEARNING ALGORITHM

        # Algorithm Parameters: step size alpha (0 or 1), small e (epsilon)
        # Initialize Q(s, a) for all states, and actions available at state s,
        #   arbitrarily except that Q(terminal) = 0

        # loop for each episode:
        #   Initialize S
        #   Choose A from S using policy derived from Q (e-greedy)
        #   loop for each step of episode: (while S is not termial)
        #       take action A, observe R, S'
        #       Choose A' from S' using policy derived from Q (e-greedy)
        #       Q(S, A) = Q(S, A) + alpha[R + learning_rate(Q(S', A')) - Q(S, A)]
        #       S = S'
        #       A = A'
    '''

    policy = [[[0.1, 0.9] for j in range(cols)] for i in range(rows)]
    for i in range(episodes):
        S = start_state


def main():
    a = 0.1
    e = 0.1
    learningRate = 0.1

    SARSA(a, e, learningRate)
