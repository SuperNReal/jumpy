class Parent():
    def __init__(self, childObj, parentObj):
        self.parent = parentObj
        self.child = childObj

        self.offSet = (0,0)
    
    def setOffSet(self, offSet):
        self.offSet = offSet
    
    def getOffSet(self):
        return self.offSet
    
    def getParentPos(self):
        return self.parent.getPosition()
    
    def getChildPos(self, relation):
        parentRect = self.parent.getRect(True)
        childRect = self.child.getRect()
        relationPos = None
        relationPlace, relationDirection = relation.split("-")
        if relationPlace == "out":
            if relationDirection == "up":
                relationPos = (parentRect.x + parentRect.w/2 - childRect.w/2, parentRect.y - childRect.h)
            elif relationDirection == "down":
                relationPos = (parentRect.x + parentRect.w/2 - childRect.w/2, parentRect.y + parentRect.h)
            elif relationDirection == "left":
                relationPos = (parentRect.x - childRect.w, parentRect.y + parentRect.h/2 - childRect.h/2)
            elif relationDirection == "right":
                relationPos = (parentRect.x + parentRect.w, parentRect.y + parentRect.h/2 - childRect.h/2)
        elif relationPlace == "in":
            if relationDirection == "center":
                relationPos = (parentRect.x + parentRect.w/2 - childRect.w/2, parentRect.y + parentRect.h/2 - childRect.h/2)
            elif relationDirection == "up":
                relationPos = (parentRect.x + parentRect.w/2 - childRect.w/2, parentRect.y)
            elif relationDirection == "down":
                relationPos = (parentRect.x + parentRect.w/2 - childRect.w/2, parentRect.y + parentRect.h - childRect.h)
            elif relationDirection == "left":
                relationPos = (parentRect.x, parentRect.y + parentRect.h/2 - childRect.h/2)
            elif relationDirection == "right":
                relationPos = (parentRect.x + parentRect.w - childRect.w, parentRect.y + parentRect.h/2 - childRect.h/2)
                
        relationPos = (relationPos[0] + self.offSet[0], relationPos[1] + self.offSet[1])
        return relationPos