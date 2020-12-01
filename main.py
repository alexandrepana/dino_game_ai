#!python3
from Game.game import *
import time
# from AI.ai import *


def __main__():
    # Game Settings
    display_graphics = True
    gamemode = 'human'
    algorithm = 'sarsa'  # 'qlearning'
    episodes = 1
    alpha = 0.1

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

        # for i in range(episodes):
        # S = state()
        # A = choose action from policy probabilities (e-greedy)
        # while time < some threshold:
        #   R = get reward for taking action
        #   S' = next state
        #   Q(S, A) = Q(S, A) + + alpha[R + learning_rate(Q(S', A')) - Q(S, A)]

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


if __name__ == '__main__':
    __main__()
