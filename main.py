#!python3
from Game.game import *
import time
from AI.policy import *
import random


def __main__():
    # Game Settings
    display_graphics = True
    gamemode = 'human'
    algorithm = 'sarsa'  # 'qlearning'
    episodes = 1
    alpha = 0.1
    learning_rate = 0.5

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

        # policy space:
        #   key: distance to next obstacle (none = no obsacles on screen)
        policy = {}
        policy["none"] = [0.5, 0.5]

        # 0: jump
        # 1: continue
        actions = [0, 1]

        for i in range(episodes):
            S = str(game.player.x - game.obstacle_manager.obstacles[0])

            # if the distance is not already been visited add it into the policy (dynamically instantiate policy)
            if not (S in policy.keys()):
                policy[S] = [0.5, 0.5]
            A = random.choice(actions) # A = random.choice(choices, weights=policy[S], k=1)

            steps = 10000
            for j in range(steps):
                S2 = 0 # simulation of S'
                R = 1 # reward for going to next state
                A2 = random.choice(actions) # A2 = random.choice(actions, weights=policy[S2], k=1)
                policy[S][A] = policy[S][A] + alpha*(R + learning_rate*(policy[S2, A2]) - policy[S][A])
                S = S2
                A = A2

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

        # policy space:
        #   key: distance to next obstacle (none = no obsacles on screen)
        policy = {}
        policy["none"] = [0.5, 0.5]

        # 0: jump
        # 1: continue
        actions = [0, 1]

        for i in range(episodes):
            S = str(game.player.x - game.obstacle_manager.obstacles[0])

            # if the distance is not already been visited add it into the policy (dynamically instantiate policy)
            if not (S in policy.keys()):
                policy[S] = [0.5, 0.5]

            steps = 10000
            for j in range(steps):
                A = random.choice(actions) # A = random.choice(choices, weights=policy[S], k=1)
                S2 = 0 # simulation of S'
                R = 1 # reward for going to next state
                A2 = 0 # get best actioin for policy[S2]
                policy[S][A] = policy[S][A] + alpha*(R + learning_rate*(policy[S2, A2]) - policy[S][A])
                S = S2


if __name__ == '__main__':
    __main__()
