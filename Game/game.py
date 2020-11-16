#!python3

import keyboard
import time
from Game import Constants
from Game.graphics import *
from Game.player import *
from Game.obstacle import *
from Game.score import *
from Game.ground import *


def play(gamemode="human", display_graphics=True):
    if display_graphics:
        win = GraphWin('Dino Game', Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        win.setBackground('white')
    
    # Define our Game Objects
    dino = Player()
    obstacle_manager = Obstacle_Manager()
    score = Score()
    ground = Ground()

    # Load Sprites
    if display_graphics:
        obstacle_manager.draw(win)
        dino.draw(win)
        score.draw(win)
        ground.draw(win)


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
            elif keyboard.is_pressed('q'):
                break
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
    print(f'Your final score is: {score.value}')
    print(f'You passed {obstacle_manager.passed} obstacles.')