#!python3
from Game.game import *
import time
# from AI.policy import *
from AI.state import *
import random


class Policy:
    def __init__(self):
        self.jumpProb = 0.5
        self.continueProb = 0.5

    def getValues(self):
        return (self.jumpProb, self.continueProb)


def __main__():
    # Game Settings
    display_graphics = False
    # gamemode = 'human'
    gamemode = 'ai'
    algorithm = 'sarsa'
    # algorithm = 'qlearning'

    episodes = 1
    alpha = 0.1
    learning_rate = 0.5

    # 0: jump
    # 1: continue
    actions = [0, 1]
    # distances = [-(Constants.UNIT_SIZE*i) for i in range(80)]
    distances = []

    # Define our windows
    if display_graphics:
        game_window = GraphWin(
            'Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setCoords(0, 0, Constants.WINDOW_WIDTH,
                              Constants.WINDOW_HEIGHT)
        game_window.setBackground('white')

        # ai_window = GraphWin('Stats', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        # ai_window.setBackground('grey')
    else:
        game_window = None
        # ai_window = None

    # Start up the game
    game = Game(game_window, gamemode, display_graphics)
    game.load_sprites()
    game.start_timer()

    if (gamemode == 'human'):
        while True:
            # Get the action to perform
            game.get_input()
            game.update_objects()
            game.update_sprites()

            if (game.over):
                game.quit()
                break

        if (game_window):
            game_window.close()

    elif (gamemode == 'ai' and algorithm == 'sarsa'):
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
        p = States(distances)

        for i in range(episodes):
            distance = game.player.x - game.obstacle_manager.obstacles[0].x
            onGround = True
            S = p.getState(distance, onGround)

            A = random.choices(actions, weights=S.policy.getValues(), k=1)[0]

            steps = 5
            for j in range(steps):
                print("S:", S.policy.getValues())
                print("DISTANCE:", S.distance)
                S2 = p.getNextState(S, A)
                print("S':", S2.policy.getValues())
                R = S2.reward
                A2 = random.choices(
                    actions, weights=S2.policy.getValues(), k=1)[0]

                updatedValue = S.policy.getValues()[A]
                updatedValue += alpha * \
                    (R + learning_rate * (S2.policy.getValues()
                                          [A2]) - S.policy.getValues()[A])
                S.policy.update(A, updatedValue)
                print("S (updated):", S.policy.getValues())

                S = S2
                A = A2

                game.update_objects()
                game.update_sprites()

    elif (gamemode == 'ai' and algorithm == 'qlearning'):
        '''
        # Q-LEARNING ALGORITHM

        # Algorithm Parameters: step size alpha (0 or 1), small e (epsilon)
        # Initialize Q(s, a) for all states, and actions available at state s,
        #   arbitrarily except that Q(terminal) = 0

        # loop for each episode:
        #   Initialize s
        #   loop for each step of episode: (while S is not terminal)
        #       choose A from S using policy derived from Q (e-greedy)
        #       take action A, observe R, S'
        #       Q(S, A) = Q(S, A) + alpha[R + learning_rate(max(Q(S', a))) - Q(S, A)]
        #       S = S'
        '''
        p = States(distances)

        for i in range(episodes):
            distance = game.player.x - game.obstacle_manager.obstacles[0].x
            onGround = True
            S = p.getState(distance, onGround)

            steps = 10000
            for j in range(steps):
                A = random.choices(
                    actions, weights=S.policy.getValues(), k=1)[0]
                S2 = p.getNextState(S, A)
                R = S2.reward
                A2 = random.choices(
                    actions, weights=S2.policy.getValues(), k=1)[0]  # TODO: get the best action available here max(policy[S2])

                updatedValue = S.policy.getValues()[A]
                updatedValue += alpha * \
                    (R + learning_rate * (S2.policy.getValues()
                                          [A2]) - S.policy.getValues()[A])
                S.policy.update(A, updatedValue)

                S = S2

        # for i in range(episodes):
        #     S = str(game.player.x - game.obstacle_manager.obstacles[0])

        #     # if the distance is not already been visited add it into the policy (dynamically instantiate policy)
        #     if not (S in policy.keys()):
        #         policy[S] = [0.5, 0.5]

        #     steps = 10000
        #     for j in range(steps):
        #         A = random.choices(actions, weights=policy[S], k=1)
        #         S2 = 0 # simulation of S'
        #         R = 1 # reward for going to next state
        #         A2 = 0 # get best actioin for policy[S2]
        #         policy[S][A] = policy[S][A] + alpha*(R + learning_rate*(policy[S2][A2]) - policy[S][A])
        #         S = S2


if __name__ == '__main__':
    __main__()
