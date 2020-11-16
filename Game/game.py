#!python3

from Game.Modules import *


class Game:
    def __init__(self, window=None, gamemode="human", display_graphics=True):
        self.gamemode = gamemode
        self.window = window
        self.over = 0
        self.just_collided = False
        self.game_objects = {}
        self.game_actions = {
            'jump': self.player_jump,
            'reset': self.reset,
            'quit': self.set_over
        }
    
    def player_jump(self):
        self.game_objects['player'].jump()

    def set_over(self):
        self.over = 1

    # Define all of our game objects
    def create_game_objects(self):
        self.game_objects['player'] = Player()
        self.game_objects['obstacle_manager'] = Obstacle_Manager()
        self.game_objects['score'] = Score()
        self.game_objects['ground'] = Ground()
    
    def get_game_objects(self):
        return self.game_objects

    def load_sprites(self):
        if (self.window):
            for game_object in self.game_objects.values():
                game_object.draw(self.window)

    # Start the score timer
    def start_timer(self):
        self.game_objects['score'].start()
    
    # If input is passed from ai, execute that. Otherwise get from user
    def get_input(self, input = None):
        if (not input):
            try:
                if (keyboard.is_pressed('w') or keyboard.is_pressed('space')) and self.game_objects['player'].grounded:  # Jump
                    input = "jump"
                elif keyboard.is_pressed('r'):                  # Reset game
                    input = "reset"
                elif keyboard.is_pressed('q'):
                    input = "quit"
                else:
                    input = None
            except:
                print('!!! ERROR !!!: something went wrong in keyboard section.')
        
        if (input):
            self.game_actions[input]()
    
    def update_objects(self):
        for game_object in self.game_objects.values():
            game_object.update()
        self.check_collisions()
    
    def update_sprites(self):
        if (self.window):
            for game_object in self.game_objects.values():
                game_object.update_draw()
            time.sleep(Constants.DELAY)     # Should we only delay if we're displaying graphics?
    
    def reset(self):
        for game_object in self.game_objects.values():
                game_object.reset()

    def quit(self):
        print(f'Your final score is: {self.game_objects["score"].value}')
        print(f'You passed {self.game_objects["obstacle_manager"].passed} obstacles.')
    
    def check_collisions(self):
        for obstacle in self.game_objects['obstacle_manager'].obstacles:
            if (self.game_objects['player'].x + self.game_objects['player'].width > obstacle.x and
                self.game_objects['player'].x < obstacle.x + obstacle.width and
                self.game_objects['player'].y + self.game_objects['player'].height > obstacle.y and
                self.game_objects['player'].y < obstacle.y + obstacle.height):
                self.game_objects['player'].sprite.setFill('red')
                self.just_collided = True