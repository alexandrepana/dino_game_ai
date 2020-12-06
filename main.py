#!python3
from Game.game import *
import matplotlib.pyplot as plt

def __main__():
    # Game Settings
    display_graphics = False
    debug_mode = False
    # display_graphics = True
    # debug_mode = True
    gamemode = 'ai'
    
    # Ai sarsa settings
    training = True
    epsilon = 0.3
    gamma = 0.9
    alpha = 0.1
    jump = 0
    stay = 0
    max_step = 1000000
    steps = max_step
    passed_count = 0

    # Define our windows
    if display_graphics:
        game_window = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setCoords(0, 0, Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setBackground('white')
    else:
        game_window = None

    # Start up the game
    game = Game(game_window, gamemode, display_graphics)
    game.load_sprites()
    game.start_timer()

    # Initialize AI
    ai = Sarsa(epsilon, gamma, alpha, jump, stay)
    # state1
    state1 = ai.get_state(game.obstacle_manager.obstacles)
    action1 = ai.select_action(state1) # action is an input, index is how we access the value
    
    #matplot
    x = []
    y = []
    run_num = 0
    
    if not (training): ai.import_policy("agent.txt")

    # Game Loop
    while (steps > 0):
        if (steps % 100000 == 0):
            print(steps)

        steps -= 1

        if (gamemode == 'human'):
            # Get the action to perform
            game.get_input()
        elif (gamemode == 'ai'):
            # Input AI action
            if(action1 == 0): game.get_input("jump")

        # Update game
        game.update_objects()
        game.update_sprites()

        
        # Get next state action space
        state2 = ai.get_state(game.obstacle_manager.obstacles)
        
        if (state2 != state1 and game.player.grounded):
            reward = 0
            

            action2 = ai.select_action(state2)

            # REWARD
            if(game.just_collided):
                reward = -5
                game.just_collided = False
                # Add to graph
                y.append(passed_count)
                x.append(run_num)
                # print(f'run #: {run_num}')
                # print(f'passed obstacles: {passed_count}')
                # print(f'current epsilon: {ai.epsilon}')
                passed_count = 0
                run_num += 1
            # if we dodged an object reward positive
            elif(passed_count < game.obstacle_manager.passed):
                passed_count = game.obstacle_manager.passed
                reward = 5
            elif(action1 == 0):
                reward = -1
            else:
                reward = 0

            if (debug_mode):
                print(f'Updating Policy:')
                print(f's:  {state1} -> \n   {state2}')
                print(f'a:  {action1} -> {action2}')
                print(f'r:  {reward}')
                print(f'e:  {ai.epsilon}')
                print(f'pc: {passed_count} / {game.obstacle_manager.passed}')
                print(f'Before: ')
                print(f'p1: {ai.policy[state1]}')
                print(f'p2: {ai.policy[state2]}')

            # Update ai
            if(training):
                ai.update_policy(state1, action1, state2, action2, reward)

            if (debug_mode):
                print(f'After: ')
                print(f'p1: {ai.policy[state1]}')
                print(f'p2: {ai.policy[state2]}')
                # input("Press Enter to continue...")

            # Remember the original state if we are no longer grounded (target will be where we land)
            # Update initial state action space
            state1 = state2
            action1 = action2

            ai.reduce_epsilon(max_step - steps)

            
            
            # if(steps%1000 == 0):
            #     fig, ax = plt.subplots()
            #     ax.plot(x,y, '-')
            #     ax.set_xlabel("Run")
            #     ax.set_ylabel("Obstacles passed")
            #     fig.savefig("GRAPH.jpg")
        
        if (game.over):
            game.quit()
            break
    
    
    # Add final info to graph
    y.append(passed_count)
    x.append(run_num)
    print(f'run #: {run_num}')
    print(f'passed obstacles: {passed_count}')
    print(f'current epsilon: {ai.epsilon}')

    # Create Graph
    fig, ax = plt.subplots()
    ax.plot(x,y, '-')
    ax.set_xlabel("Run")
    ax.set_ylabel("Obstacles passed")
    fig.savefig("GRAPH.jpg")

    ai.print_policy()
    if(training): ai.export_policy("agent.txt")
    
    if (game_window):
        game_window.close()

if __name__ == '__main__':
    __main__()