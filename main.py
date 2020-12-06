#!python3
from Game.game import *
import matplotlib.pyplot as plt


def __main__():
    # Game Settings
    display_graphics = False
    gamemode = 'ai'
    # learning = 'sarsa'
    learning = 'qlearning'

    # Ai sarsa settings
    training = True
    epsilon = 0.9
    gamma = 0.5
    alpha = .95
    jump = 0.2
    stay = 0.8
    max_step = 10000
    steps = max_step
    passed_count = 0

    # Define our windows
    if display_graphics:
        game_window = GraphWin(
            'Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setCoords(0, 0, Constants.WINDOW_WIDTH,
                              Constants.WINDOW_HEIGHT)
        game_window.setBackground('white')
    else:
        game_window = None

    # Start up the game
    game = Game(game_window, gamemode, display_graphics)
    game.load_sprites()
    game.start_timer()

    # Initialize AI
    ai = Sarsa(epsilon, gamma, alpha, jump, stay)
    if (learning == 'qlearning'):
        ai = QLearning(epsilon, gamma, alpha, jump, stay)

    state1 = ai.get_state(game.obstacle_manager.obstacles)
    # action is an input, index is how we access the value
    action1 = ai.select_action(state1)

    # matplot
    x = []
    y = []

    if not (training):
        ai.import_policy("agent.txt")

    # Game Loop
    while (steps > 0):
        reward = 0
        steps -= 1

        if (gamemode == 'human'):
            # Get the action to perform
            game.get_input()
        elif (gamemode == 'ai'):
            # Input AI action
            if(action1 == 0):
                game.get_input("jump")

        # Update game
        game.update_objects()
        game.update_sprites()

        # if we hit an object make a large negative rewardqq
        if(game.just_collided):
            reward = -20
        # # if we dodged an object reward positive
        # elif(passed_count < game.obstacle_manager.passed):
        #     passed_count += 1
        #     reward += 20
        # elif(action1 == "jump"):
        #     reward -= 10

        if (learning == 'sarsa'):
            # Get next state action space
            state2 = ai.get_state(game.obstacle_manager.obstacles)
            # print(index1)
            action2 = ai.select_action(state2)
        else:
            simJump = game
            simCont = game
            jumpReward = 0
            contReward = 0

            simJump.get_input('jump')
            simJump.update_objects()
            simJump.update_sprites

            simCont.get_input()
            simCont.update_objects()
            simCont.update_sprites()

            if (simJump.just_collided):
                jumpReward = -20
            if (simCont.just_collided):
                contReward = -20

            state2 = ai.get_state(game.obstacle_manager.obstacles)
            action2 = ai.select_action(state2)
            if (jumpReward > contReward):
                action2 = 0
            if (contReward > jumpReward):
                action2 = 1

        # Update ai
        if(training):
            ai.update_policy(state1, action1, state2, action2, reward)

        # Remember the original state if we are no longer grounded (target will be where we land)
        if(game.player.grounded == 1):
            # Update initial state action space
            state1 = state2
            action1 = action2

        if (game.over):
            game.quit()
            break

        if(steps % 100 == 0):
            y.append(game.obstacle_manager.passed)
            x.append(max_step - steps)
            fig, ax = plt.subplots()
            ax.plot(x, y, '-')
            ax.set_xlabel("Step")
            ax.set_ylabel("Obstacles passed")
            fig.savefig("GRAPH.jpg")

    ai.print_policy()
    if(training):
        ai.export_policy("agent.txt")

    if (game_window):
        game_window.close()


if __name__ == '__main__':
    __main__()
