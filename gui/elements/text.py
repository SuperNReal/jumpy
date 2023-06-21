import pygame

from gui.other.parent import Parent
from gui.other.colors import Colors


class Text():
    def __init__(self, font, text, size, position, color=Colors.black):
        self.font = font
        self.text = text
        self.size = size
        self.pos = position
        self.color = color

        self.parent = None
        self.parentRelation = None

    
    def setFont(self, font):
        self.font = font
    
    def setText(self, text):
        self.text = text
    
    def setSize(self, size):
        self.size = size
    
    def setPosition(self, position):
        self.pos = position
    
    def setColor(self, color):
        self.color = color
    
    def setParent(self, guiObj, offSet):
        self.parent = Parent(self, guiObj)
        self.parent.setOffSet(offSet)
    
    def setParentRelation(self, parentRelation):
        self.parentRelation = parentRelation
    
    
    def getFont(self):
        return self.font
    
    def getText(self):
        return self.text
    
    def getSize(self):
        return self.size
    
    def getPosition(self):
        return self.pos
    
    def getColor(self):
        return self.color
    
    def getRect(self, isUseParent=False):
        rect = pygame.font.Font(self.font, self.size).render(self.text, True, self.color).get_rect()

        if isUseParent and not self.parentRelation is None:
            rect.x, rect.y = self.parent.getChildPos(self.parentRelation)
        else:
            rect.x, rect.y = self.pos
        return rect

    def getParent(self):
        return self.parent
    
    def getParentRelation(self):
        return self.parentRelation
    

    def render(self, surface):
        if self.text == "":
            return
        font = pygame.font.Font(self.font, self.size)
        textRender = font.render(self.text, True, self.color)
        
        if self.parentRelation is None:
            pos = self.pos
        else:
            pos = self.parent.getChildPos(self.parentRelation)

        surface.blit(textRender, pos)