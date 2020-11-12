#!python3

import keyboard
import time
import Constants
from graphics import *
from player import *
from obstacle import *


def main():
    display_graphics = 1    # Set to false if you don't want to display the graphics
    if display_graphics:
        win = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        win.setBackground('white')
    dino = Player()

    obstacle1 = Obstacle()


    # Load Sprites
    if display_graphics:
        obstacle1.draw(win)     # draw obstacle
        dino.draw(win)          # draw player


    # Game Loop
    while True:
        try:
            if keyboard.is_pressed('w') and dino.grounded:
                dino.jump()
        except:
            print('no')

        obstacle1.update()
        dino.update()

        # Sprite Updates
        if display_graphics:
            obstacle1.update_draw()
            dino.update_draw()
            time.sleep(Constants.DELAY)     # Should we only delay if we're displaying graphics?
            
        
    
    # Game Over
    win.close()
    
    
        



main()

