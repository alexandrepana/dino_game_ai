#!python3

import keyboard
import time
from graphics import *
from player import *
from obstacle import *


def main():
    display_graphics = 1    # Set to false if you don't want to display the graphics
    if display_graphics:
        win = GraphWin('Dino Game', 750, 500)
    dino = Player()
    obstacle1 = Obstacle(win.width)

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
        
        time.sleep(0.05)
    
    # Game Over
    win.close()
    
        



main()

