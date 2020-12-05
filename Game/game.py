#!python3
from Game.Modules import *

class Game:
    def __init__(self, window=None, gamemode="human", display_graphics=True):
        # Game Variables
        self.gamemode = gamemode
        self.window = window
        self.over = 0
        self.just_collided = False
        self.high_score = 0
        
        # Game Objects
        self.player = Player()
        self.obstacle_manager = Obstacle_Manager()
        self.score = Score()
        self.high_score = High_Score()
        self.ground = Ground()

        # Possible Actions
        self.game_actions = {
            'jump': self.player_jump,
            'reset': self.reset,
            'quit': self.set_over
        }
    
    def player_jump(self):
        self.player.jump()

    def set_over(self):
        self.over = 1
    
    # PROGRAM THIS
    def get_game_objects(self):
        return (self.player, self.obstacle_manager, self.score, self.ground)

    def load_sprites(self):
        if (self.window):
            self.player.draw(self.window)
            self.obstacle_manager.draw(self.window)
            self.score.draw(self.window)
            self.high_score.draw(self.window)
            self.ground.draw(self.window)

    # Start the score timer
    def start_timer(self):
        self.score.start()
    
    # If input is passed from ai, execute that. Otherwise get from user
    def get_input(self, input = None):
        if (not input):
            try:
                if (keyboard.is_pressed('w') or keyboard.is_pressed('space')) and self.player.grounded:  # Jump
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
        # self.game_objects.function('update', self.window)
        self.player.update()
        self.obstacle_manager.update()
        self.score.update()
        self.high_score.update(self.score.value)
        self.ground.update()
        self.check_collisions()
    
    def update_sprites(self):
        if (self.window):
            self.player.update_draw()
            self.obstacle_manager.update_draw()
            self.score.update_draw()
            self.high_score.update_draw()
            self.ground.update_draw()
            time.sleep(Constants.DELAY)     # Should we only delay if we're displaying graphics?
    
    def reset(self):
        self.player.reset()
        self.obstacle_manager.reset()
        self.score.reset()
        self.ground.reset()

    def quit(self):
        print(f'Your final score is: {self.score.value}')
        print(f'You passed {self.obstacle_manager.passed} obstacles.')
    
    def check_collisions(self):
        for obstacle in self.obstacle_manager.obstacles:
            if (self.player.x + self.player.width > obstacle.x and
                self.player.x < obstacle.x + obstacle.width and
                self.player.y + self.player.height > obstacle.y and
                self.player.y < obstacle.y + obstacle.height):
                self.player.change_colour()
                self.just_collided = True
                self.score.reset()
                self.obstacle_manager.reset()

    def check_dodge(self):
        for obstacle in self.obstacle_manager.obstacles:
            if (self.player.x + self.player.width > obstacle.x and
                self.player.x < obstacle.x + obstacle.width and
                self.player.y + self.player.height < obstacle.y and
                self.player.y > obstacle.y + obstacle.height):
                return True
            else:
                return False
    
    def update_high_score(self):
        if (self.score.value > self.high_score):
            self.high_score = self.score.value