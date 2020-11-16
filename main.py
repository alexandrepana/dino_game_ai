#!python3
from Game.game import *
from AI.ai import *


def __main__():
    # Game Settings
    display_graphics = True
    gamemode = 'human'
    
    # Define our windows
    if display_graphics:
        game_window = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setCoords(0, 0 ,Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        game_window.setBackground('white')

        # ai_window = GraphWin('Stats', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        # ai_window.setBackground('grey')
    else:
        game_window = None
        # ai_window = None

    game = Game(game_window, gamemode, display_graphics)

    game.load_sprites()

    game.start_timer()

    # Game Loop
    while True:
        game.get_input()
        # game.get_input(ai.next_input)

        game.update_objects()

        game.update_sprites()

        reward = game.just_collided

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