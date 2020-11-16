#!python3
from Game.game import *
from AI.ai import *


def __main__():
    # Game Settings
    display_graphics = True
    gamemode = 'human'
    
    # Define our window
    if display_graphics:
        win = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        win.setBackground('white')
    else:
        win = None

    game = Game(win, gamemode, display_graphics)
    # game.play(gamemode, display_graphics)

    # game.create_game_objects()

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

    if (win):
        win.close()


if __name__ == '__main__':
    __main__()