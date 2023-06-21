import pygame

from gui.other.colors import Colors


class Rectangle():
    def __init__(self, size:tuple, position:tuple, color=Colors.white):
        self.size = size
        self.pos = position
        self.color = color
    
    
    def setSize(self, size:tuple):
        self.size = size
    
    def setPosition(self, position:tuple):
        self.pos = position
    
    def setColor(self, color:tuple):
        self.color = color
    
    
    def getSize(self):
        return self.size
    
    def getPosition(self):
        return self.pos

    def getColor(self):
        return self.color
    
    def getRect(self, isUseParent=False):
        return pygame.Rect(self.pos, self.size)
    

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.getRect())
        pygame.draw.rect(surface, Colors.black, self.getRect(), 3)