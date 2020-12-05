#!python3
from Game.game import *
from AI.sarsa import Sarsa



def __main__():
    # Game Settings
    display_graphics = True
    gamemode = 'human'
    
    # Ai sarsa settings
    epsilon = 0.1
    gamma = 0.85
    alpha = 0.95
    thresholds = []
    jump = 0.2
    stay = 0.8
    # partition the screen into state spaces
    for x in range(0, 1, 0.1):
        thresholds.append(Constants.WINDOW_WIDTH * x)
    
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

    # Start up AI
    ai = Sarsa(epsilon, gamma, alpha, thresholds, jump, stay)

    # Game Loop
    while True:
        # Get the action to perform
        if (gamemode == 'human'):
            game.get_input()
        elif (gamemode == 'ai'):
            game.get_input(ai.select())

        game.update_objects()

        game.update_sprites()

        # reward = game.just_collided

        if (game.over):
            game.quit()
            break

        # ai.get_state(game.get_game_objects())

        # ai.update_state()

        # ai.update_policy(reward)

        # ai.draw_state()

        # ai_input = ai.predict()

    if (game_window):
        game_window.close()

if __name__ == '__main__':
    __main__()