from pygame import Rect


class Collistion():
    def checkCollistion(rect, targetRect, xVelocity, yVelocity):
        targetRectSize = 25
        rectYHeight = 15
        rectXSizeCorrection = 3
    
        targetUpRect = Rect(targetRect.x, targetRect.y - 1, targetRect.w, targetRectSize)
        targetDownRect = Rect(targetRect.x, targetRect.y + targetRect.h - targetRectSize + 1, targetRect.w, targetRectSize)
        targetLeftRect = Rect(targetRect.x - 1, targetRect.y, targetRectSize, targetRect.h)
        targetRightRect = Rect(targetRect.x + targetRect.w - targetRectSize + 1, targetRect.y, targetRectSize, targetRect.h)

        rectUpRect = Rect(rect.x + xVelocity, rect.y + yVelocity, rect.w, rectYHeight)
        rectDownRect = Rect(rect.x + xVelocity, rect.y + rect.h - rectYHeight + yVelocity, rect.w, rectYHeight)
        rectLeftRect = Rect(rect.x + xVelocity, rect.y + rectXSizeCorrection, rect.w/4, rect.h - rectXSizeCorrection)
        rectRightRect = Rect(rect.x + rect.w - rect.w/4 + xVelocity, rect.y + rectXSizeCorrection, rect.w/4, rect.h - rectXSizeCorrection)

        finalPos = ""
        xVelocityFix = 0
        yVelocityFix = 0

        downOfRect = rectDownRect.colliderect(targetUpRect)
        upOfRect = rectUpRect.colliderect(targetDownRect)
        leftOfRect = rectLeftRect.colliderect(targetRightRect)
        rightOfRect = rectRightRect.colliderect(targetLeftRect)


        if rightOfRect:
            finalPos += "right"
            if targetRect.x > rect.x + rect.w:
                xVelocityFix = targetRect.x - rect.w - 1
        elif leftOfRect:
            finalPos += "left"
            if targetRect.x + targetRect.w > rect.x:
                xVelocityFix = targetRect.x + targetRect.w + 1
        elif downOfRect:
            finalPos += "down"
            if targetRect.y > rect.y + rect.h:
                yVelocityFix = targetRect.y - rect.h - 1
        elif upOfRect:
            finalPos += "up"
            if targetRect.y + targetRect.h < rect.y:
                yVelocityFix = targetRect.y + targetRect.h + 1

        # finalPos += "-in"

        # TODO: try to make collistion more accurate by adding what edge it touches 
        # if downOfRect or upOfRect:
        #     rectLeftRect.y -= rectXSizeCorrection
        #     rectLeftRect.h += rectXSizeCorrection

        #     if rectLeftRect.colliderect(targetRightRect):
        #         print ("ez")
        # elif rightOfRect or leftOfRect:
        #     pass

        
        if finalPos == "":
            return "no", xVelocityFix, yVelocityFix
        else:
            return finalPos, xVelocityFix, yVelocityFix