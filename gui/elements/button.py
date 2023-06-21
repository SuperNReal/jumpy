import pygame

from gui.other.parent import Parent
from gui.other.colors import Colors

from gui.elements.text import Text


class Button():
    def __init__(self, font:str, text:str, textSize:int, size:tuple, position:tuple, colorOff=Colors.yellow, colorOn=Colors.blue, colorBorder=Colors.black):
        self.text = Text(font, text, textSize, (0,0))
        self.text.setParent(self, (0,0))
        self.text.setParentRelation("in-center")
        self.size = size
        self.pos = position
        self.colorOff = colorOff
        self.colorOn = colorOn
        self.colorBorder = colorBorder
        self.parent = Parent(self, None)
        self.parentRelation = None

        self.colorSwitch = colorOff
    
    
    def setSize(self, size):
        self.size = size
    
    def setPosition(self, position):
        self.pos = position
    
    def setColorOff(self, color):
        self.colorOff = color
    
    def setColorOn(self, color):
        self.colorOn = color
    
    def setColorBorder(self, color):
        self.colorBorder = color
    
    def setParent(self, guiObj, offSet):
        self.parent = Parent(self, guiObj)
        self.parent.setOffSet(offSet)
    
    def setParentRelation(self, parentRelation):
        self.parentRelation = parentRelation

    
    def getText(self):
        return self.text
    
    def getSize(self):
        return self.size
    
    def getColorOff(self):
        return self.colorOff
    
    def getColorOn(self):
        return self.colorOn
    
    def getColorBorder(self):
        return self.colorBorder
    
    def getRect(self, isUseParent=False):
        rect = pygame.Rect(self.pos, self.size)

        if isUseParent and not self.parentRelation is None:
            rect.x, rect.y = self.parent.getChildPos(self.parentRelation)
        
        return rect
    
    def getParent(self):
        return self.parent
    
    def getParentRelation(self):
        return self.parentRelation
    

    def checkCollision(self, cursorPosition):
        if self.getRect(True).collidepoint(cursorPosition):
            return True
        else:
            return False

    def update(self):
        mousePos = pygame.mouse.get_pos()
        if self.checkCollision(mousePos):
            self.colorSwitch = self.colorOn
        else:
            self.colorSwitch = self.colorOff

    def render(self, surface):
        pygame.draw.rect(surface, self.colorSwitch, self.getRect(True))
        pygame.draw.rect(surface, self.colorBorder, self.getRect(True), 3)
        self.text.render(surface)