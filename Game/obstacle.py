#!python3
from Game.Modules import *


# Our Player Class
class Obstacle(Game_Object):
    def __init__(self):
        self.randomize_x()
        self.y = Constants.GROUND
        self.height = 30
        self.width = 25
        self.speed = 16
        self.sprite = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
        self.sprite.setFill = 'red'

    def randomize_x(self):
        self.x = Constants.WINDOW_WIDTH + random.randrange(0, Constants.WINDOW_HEIGHT * 1.5)

    # This is handled in the obstacle manager now
    def update(self):
        pass

    def draw(self, win):
        self.sprite.draw(win)

    def update_draw(self):
        # These are specifically for rectangles
        old_corner1 = self.sprite.getP1()
        self.sprite.move(self.x - old_corner1.getX(), self.y - old_corner1.getY())
    
    def reset(self):
        pass


class Obstacle_Manager(Game_Object):
    def __init__(self):
        self.obstacles = [ Obstacle() for i in range(Constants.NUM_OBSTACLES) ]
        self.min_obstacle_dist = 70
        self.passed = 0
        self.passed_string = f'Obstacles Passed: {self.passed}'
        self.sprite = Text(Point(Constants.WINDOW_WIDTH / 2 - 15, 25), self.passed_string)

        for obstacle in self.obstacles:
            self.randomize_x(obstacle)
    
    def randomize_x(self, obstacle):
        valid_x = False
        while (not valid_x):
            valid_x = True
            obstacle.randomize_x()

            for other_obstacle in self.obstacles:
                if obstacle != other_obstacle:
                    if obstacle.x + obstacle.width > other_obstacle.x - self.min_obstacle_dist and obstacle.x < other_obstacle.x + other_obstacle.width + self.min_obstacle_dist:
                        valid_x = False
  
    def update(self):
        for obstacle in self.obstacles:
            obstacle.x -= obstacle.speed

            # Check if Obstacle is off-screen
            if (obstacle.x <= -obstacle.width):
                self.passed += 1
                self.randomize_x(obstacle)
            
        
    def draw(self, win):
        self.sprite.draw(win)
        for obstacle in self.obstacles:
            obstacle.draw(win)
    
    def update_draw(self):
        for obstacle in self.obstacles:
            obstacle.update_draw()
            self.sprite.setText(f'Obstacles Passed: {self.passed}')
    
    def reset(self):
        for obstacle in self.obstacles:
            self.randomize_x(obstacle)
        self.passed = 0