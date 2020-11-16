#!python3
from Game.Modules import *
from abc import ABC, abstractmethod

class Game_Object(ABC):
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def draw(self, win):
        pass

    @abstractmethod
    def update_draw(self):
        pass

    @abstractmethod
    def reset(self):
        pass