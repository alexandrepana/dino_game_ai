#!python3

import keyboard
import time
import Constants
from graphics import *
from player import *
from obstacle import *
from score import *


def main():
    display_graphics = 1    # Set to false if you don't want to display the graphics
    if display_graphics:
        win = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        win.setBackground('white')
    
    dino = Player()
    obstacle_manager = Obstacle_Manager()
    score = Score()

    # Load Sprites
    if display_graphics:
        obstacle_manager.draw(win)
        dino.draw(win)
        score.draw(win)


    # Game Loop
    score.start()
    while True:
        # Get Player Input
        try:
            if (keyboard.is_pressed('w') or keyboard.is_pressed('space')) and dino.grounded:  # Jump
                dino.jump()
            elif keyboard.is_pressed('r'):                  # Reset game
                dino.reset()
                score.reset()
                obstacle_manager.reset()
        except:
            print('!!! ERROR !!!: something went wrong in keyboard section.')

        # Game Updates
        dino.update(obstacle_manager)
        obstacle_manager.update()
        score.update()

        # Sprite Updates
        if display_graphics:
            obstacle_manager.update_draw()
            dino.update_draw()
            score.update_draw()
            time.sleep(Constants.DELAY)     # Should we only delay if we're displaying graphics?
            
        
    # Game Over
    win.close()
    
    
        



main()

