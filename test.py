#!python3
from Game.game import *

# Game Settings
display_graphics = True
gamemode = 'human'

# Ai sarsa settings
training = True
epsilon = 0.1
gamma = 0.85
alpha = 0.95
jump = 0.2
stay = 0.8
    
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

# Ai sarsa settings
training = True
epsilon = 0.1
gamma = 0.85
alpha = 0.95
jump = 0.2
stay = 0.8

# Initialize AI
ai = Sarsa(epsilon, gamma, alpha, jump, stay)
ai.import_policy("agent.txt")
ai.print_policy()

