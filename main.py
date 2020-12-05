#!python3
from Game.game import *

def __main__():
    # Game Settings
    display_graphics = False
    gamemode = 'ai'
    
    # Ai sarsa settings
    training = True
    epsilon = 0.1
    gamma = 0.85
    alpha = 0.95
    jump = 0.2
    stay = 0.8
    episodes = 10000
    
    # Define our windows
    if display_graphics:
        game_window = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setCoords(0, 0 ,Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setBackground('white')
    else:
        game_window = None

    # Start up the game
    game = Game(game_window, gamemode, display_graphics)
    game.load_sprites()
    game.start_timer()

    # Initialize AI
    ai = Sarsa(epsilon, gamma, alpha, jump, stay)
    state1 = ai.get_state(game.obstacle_manager.obstacles)
    print(state1)
    action1, index1 = ai.select_action(state1) # action is an input, index is how we access the value
    reward = 0

    # Game Loop
    while (episodes > 0):
       
        episodes -= 1

        if (gamemode == 'human'):
            # Get the action to perform
            game.get_input()
        elif (gamemode == 'ai'):
            # Input AI action
            game.get_input(action1) # will only work if the player is grounded

        # Update game
        game.update_objects()
        game.update_sprites()

        # if we hit an object make a large negative reward
        if(game.just_collided):
            reward -= 100
        # if we dodged an object reward positive
        elif(game.check_dodge):
            reward += 20
        elif(action1 == "jump"):
            reward -=10
        
        # Get next state action space
        state2 = ai.get_state(game.obstacle_manager.obstacles)
        action2, index2 = ai.select_action(state2)

        # Update ai
        if(training): ai.update_policy(state1, index1, state2, index2, reward)

        # Remember the original state if we are no longer grounded (target will be where we land)
        if(game.player.grounded == 1):
            # Update initial state action space
            state1 = state2
            action1 = action2

        if (game.over):
            game.quit()
            break

    ai.print_policy()
    
    if (game_window):
        game_window.close()

if __name__ == '__main__':
    __main__()