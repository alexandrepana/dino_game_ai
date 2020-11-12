#!python3

import keyboard
import time
from graphics import *
from player import *
from obstacle import *

# Constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 750


def main():
    display_graphics = 0    # Set to false if you don't want to display the graphics
    if display_graphics:
        win = GraphWin('Dino Game', WINDOW_HEIGHT, WINDOW_WIDTH)
    dino = Player()
    obstacle1 = Obstacle(WINDOW_WIDTH)

    # Game Loop
    while True:
        try:
            if keyboard.is_pressed('w') and dino.grounded:
                dino.jump()
        except:
            print('no')

        obstacle1.update()
        dino.update()

        # Canvas Updates
        if display_graphics:
            # win.update()
            background = Rectangle(Point(0, 0), Point(win.width, win.height))
            background.setFill('white')
            background.draw(win)    # clear screen
            obstacle1.draw(win)     # draw obstacle
            dino.draw(win)          # draw player
        
    
    # Game Over
    win.close()
    
    
        



main()

