#!python3
from Game.game import *
import time
from AI.policy import *
from AI.state import *
import random
import matplotlib.pyplot as plt

epsilon = 0.1


def epsilon_greedy(state_policy, actions):

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
    display_graphics = False
    # gamemode = 'human'
    gamemode = 'ai'
    # algorithm = 'sarsa'
    algorithm = 'qlearning'

    episodes = 10000
    a = 0.5
    r = 0.1

    action_decision = {
        "probabilistic": False,
        "epsilon_greedy": True
    }

    # 0: jump
    # 1: continue
    actions = [0, 1]
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
    # episode_label = Text(Point(Constants.WINDOW_WIDTH /
    #                            2 + 150, 25), "Episode: 0").draw(game_window)

    # p = importPolicy("testFile.txt")
    p = States(distances)

    # episode_label = Text(Point(Constants.WINDOW_WIDTH /
    #                            2 + 150, 25), "Episode: 0").draw(game_window)

    # For graphing:
    x = []  # Episodes
    y = []  # Obstacles passed per episode

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

        for i in range(episodes):
            print("EPISODE:", i)
            # episode_label.setText("Episode: " + str(i))
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

            steps = 0
            # loop for each step of episode (while S is not terminal)
            # for j in range(steps):
            while game.obstacle_manager.passed < 20:

                # take action A
                if (A == 0):
                    game.get_input('jump')
                else:
                    game.get_input()

                game.update_objects()
                game.update_sprites()

                # observe R, S'
                distance = game.player.x - game.obstacle_manager.obstacles[0].x
                S2 = p.getState(distance, False)

                R = 0
                if game.get_collided():
                    R = -100
                    # print("Oof, A caused a collision")
                elif game.check_dodge():
                    R = 100

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

            # Graphing
            y.append(game.obstacle_manager.obstacle_score)
            x.append(i)

        plt.clf()
        fig, ax = plt.subplots()
        ax.plot(x, y, '-')
        ax.set_xlabel("Episodes")
        ax.set_ylabel("Steps per Episode")
        fig.savefig("SARSA(a={}r={}e={}).jpg".format(a, r, epsilon))

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

        for i in range(episodes):
            print("EPISODE:", i)
            # episode_label.setText("Episode: " + str(i))
            game.obstacle_manager.passed = 0
            distance = game.player.x - game.obstacle_manager.obstacles[0].x

            onGround = game.player.grounded

            # Initialize S
            S = p.getState(distance, onGround)

            steps = 5000
            # loop for each step of episode (while S is not terminal)
            # for j in range(steps):
            while game.obstacle_manager.passed < 20:
                # Choose A from S using policy derived from Q
                A = None

                if action_decision["probabilistic"]:
                    # Choose A from S using policy derived from Q
                    A = random.choices(
                        actions, weights=S.policy.getValues(), k=1)[0]
                elif action_decision["epsilon_greedy"]:
                    # Choose the BEST action A (given in policy)
                    # with probability 1 - epsilon + epsilon/len(actions)
                    A = epsilon_greedy(S.policy.getValues(), actions)

                # take action A
                if (A == 0):
                    game.get_input('jump')
                else:
                    game.get_input()

                game.update_objects()
                game.update_sprites()

                # observe R, S'
                distance = game.player.x - game.obstacle_manager.obstacles[0].x
                S2 = p.getState(distance, False)

                R = 0
                if game.get_collided():
                    R = -100
                    # print("Oof, A caused a collision")
                elif game.check_dodge():
                    R = 100
                elif A == 0:
                    R = -10

                # find max(A(S', a))
                simJump = game.simulate_input('jump')
                simContinue = game.simulate_input()

                simJump.update_objects()
                simJump.update_sprites()
                simContinue.update_objects()
                simContinue.update_sprites()

                jumpReward = -10
                continueReward = 0

                if (simJump.get_collided()):
                    jumpReward = -100
                elif (simJump.check_dodge()):
                    jumpReward = 100
                if (simContinue.get_collided()):
                    continueReward = -100
                elif(simContinue.check_dodge()):
                    continueReward = 100

                # arbitrarily choose A2
                A2 = random.choices(actions, [1, 1], k=1)[0]

                # get max option for A2 if available
                if (jumpReward > continueReward):
                    A2 = 0
                if (continueReward > jumpReward):
                    A2 = 1

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

            # Graphing
            y.append(game.obstacle_manager.obstacle_score)
            x.append(i)

        plt.clf()
        fig, ax = plt.subplots()
        ax.plot(x, y, '-')
        ax.set_xlabel("Episodes")
        ax.set_ylabel("Steps per Episode")
        fig.savefig("QLearning(a={}r={}e={}).jpg".format(a, r, epsilon))

    elif (gamemode == 'ai' and algorithm == 'sarsa2'):
        '''
        Input: a feature function
        Input: a policy (p)
        Algorithm Parameters: step size a > 0, trace decay rate lambda [1, 0]
        Initialize weight vector in with dimension d

        loop for each episode:
            Initialize S
            Choose A from p(S)
            x = x(S, A)
            z = 0
            Qold = 0
            loop for each step of the episode: (until S' is terminal)
                Take action A
                Observe R, S'
                Choose A' from p(S)
                x' = s(S', A')
                Q = Transpose(W)*x
                Q' = transpose(W)x'
                delta = R + v*Q' - A
                z = v*decayRate*z + (1 - a*v*decayRate*transpose(z)*x)*x
                w = w + a(delta + Q - Qold)*z) - a(Q - Qold)*x
                Qold = Q'
                x = x'
                A = A'
        '''
        for i in range(episodes):
            S = State()
            A = random.choices(actions, weights=S.policy.getValues(), k=1)[0]


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
