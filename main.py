#!python3
from Game.game import *
import time
# from AI.policy import *
from AI.state import *
import random


class Policy:
    def __init__(self):
        self.jumpProb = 0.2
        self.continueProb = 0.8

    def getValues(self):
        return (self.jumpProb, self.continueProb)


def epsilon_greedy(state_policy, actions):
    epsilon = 0.1

    # Chooses whether to go epsilon or the greedy path, ensures exploration
    epsilon_choice = random.choices(["Greedy", "Epsilon"],
                                    weights=[1 - epsilon + epsilon /
                                             len(actions), epsilon/len(actions)],
                                    k=1)
    if epsilon_choice == "Greedy":
        return state_policy.index(max(state_policy))
    else:
        return state_policy.index(random.choice(state_policy))


def __main__():
    # Game Settings
    display_graphics = True
    # gamemode = 'human'
    gamemode = 'ai'
    algorithm = 'sarsa'
    # algorithm = 'qlearning'

    episodes = 1
    a = 0.1
    r = 0.1

    action_decision = {
        "probabilistic": False,
        "epsilon_greedy": True
    }

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
        # p = importPolicy("testFile.txt")
        p = States(distances)

        episode_label = Text(Point(Constants.WINDOW_WIDTH /
                                   2 + 150, 25), "Episode: 0").draw(game_window)

        for i in range(episodes):
            print("EPISODE:", i)
            episode_label.setText("Episode: " + str(i))
            game.obstacle_manager.passed = 0
            distance = game.player.x - game.obstacle_manager.obstacles[0].x

            onGround = game.player.grounded

            # Initialize S
            S = p.getState(distance, onGround)
            A = None

            if action_decision["probabilistic"]:
                # Choose A from S using policy derived from Q
                A = random.choices(
                    actions, weights=S.policy.getValues(), k=1)[0]
            elif action_decision["epsilon_greedy"]:
                # Choose the BEST action A (given in policy)
                # with probability 1 - epsilon + epsilon/len(actions)
                A = epsilon_greedy(S.policy.getValues(), actions)

            steps = 5000
            # loop for each step of episode (while S is not terminal)
            # for j in range(steps):
            while game.obstacle_manager.passed < 20:

                # take action A
                if (A == 0):
                    game.get_input('jump')
                    # print("Jumping")
                # else:
                    # print("Continuing")
                # observe R, S'
                distance = game.player.x - game.obstacle_manager.obstacles[0].x
                S2 = p.getState(distance, False)

                R = 0
                if game.get_collided():
                    R = -100
                    print("Oof, A caused a collision")

                # Choose A' from S' using policy derived from Q (e-greedy)
                if action_decision["probabilistic"]:
                    # Choose A from S using policy derived from Q
                    A2 = random.choices(
                        actions, weights=S2.policy.getValues(), k=1)[0]

                elif action_decision["epsilon_greedy"]:
                    # Choose the BEST action A (given in policy)
                    # with probability 1 - epsilon + epsilon/len(actions)
                    A2 = epsilon_greedy(S2.policy.getValues(), actions)

                # Q(S, A) = Q(S, A) + alpha[R + learning_rate(Q(S', A')) - Q(S, A)]
                updatedValue = S.policy.getValues()[A]
                updatedValue += a * \
                    (R + r * (S2.policy.getValues()
                              [A2]) - S.policy.getValues()[A])
                S.policy.update(A, updatedValue)

                if (game.player.grounded == 1):
                    S2 = p.getState(distance, True)

                # End the episode after calculating the Q value of a collision
                if game.get_collided():
                    game.set_collided(False)
                    break

                # S = S'
                S = S2
                # A = A'
                A = A2

                game.update_objects()
                game.update_sprites()

        print("POLICY:")
        for key in p.tStates.keys():
            print(key, ": ", p.tStates[key].policy.getValues())

        exportPolicy(p, "testFile.txt")

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
            onGround = game.player.grounded

            # Initialize S
            S = p.getState(distance, onGround)

            steps = 5000
            # loop for each step of episode (while S is not terminal)
            # for j in range(steps):
            while game.obstacle_manager.passed < 25:
                # Choose A from S using policy derived from Q
                A = random.choices(
                    actions, weights=S.policy.getValues(), k=1)[0]
                # take action A
                if (A == 0):
                    game.get_input('jump')

                # observe R, S'
                distance = game.player.x - game.obstacle_manager.obstacles[0].x
                S2 = p.getState(distance, False)
                if (game.player.grounded == 1):
                    S2 = p.getState(distance, True)

                R = 0
                if (distance > 0 and game.player.grounded == 1):
                    R = -10
                elif (distance > 0 and game.player.grounded == 0):
                    R = 10

                # Choose A' from S' using policy derived from Q (e-greedy)
                A2 = random.choices(
                    actions, weights=S2.policy.getValues(), k=1)[0]

                # Q(S, A) = Q(S, A) + alpha[R + learning_rate(Q(S', A')) - Q(S, A)]
                updatedValue = S.policy.getValues()[A]
                updatedValue += a * \
                    (R + r * (S2.policy.getValues()
                              [A2]) - S.policy.getValues()[A])
                S.policy.update(A, updatedValue)

                # S = S'
                S = S2

                game.update_objects()
                game.update_sprites()


def exportPolicy(p, fileName):
    with open(fileName, 'w') as f:
        for key in p.tStates.keys():
            item = "t, {}, {}, {}".format(key, p.tStates[key].policy.getValues()[
                0], p.tStates[key].policy.getValues()[1])
            f.write("%s\n" % item)
        for key in p.fStates.keys():
            item = "f, {}, {}, {}".format(key, p.tStates[key].policy.getValues()[
                0], p.tStates[key].policy.getValues()[1])
            f.write("%s\n" % item)


def importPolicy(fileName):
    p = States()

    with open(fileName, 'r') as f:
        contents = f.readlines()

    for state in contents:
        info = state.split(', ')

        # initialize state object for this state entry
        s = State()

        # set distance for state object
        s.distance = int(info[1])

        # initialize and set policy for state object
        s.policy.jumpProb = float(info[1])
        s.policy.continueProb = float(info[1])

        # add initialized state object (with relevant information) to the policy's states at the proper key
        if (info[0] == "t"):
            p.tStates[info[1]] = s
        elif (info[0] == "f"):
            p.fStates[info[1]] = s

    return p


if __name__ == '__main__':
    __main__()
