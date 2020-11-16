#!python3
from Game import game



def __main__():
    # Define Game Settings
    display_graphics = True    # Set to 0 if you don't want to display the graphics
    gamemode = 'human'
    
    game.play(gamemode, display_graphics)


if __name__ == '__main__':
    __main__()