import pygame
from pygame import display as dis, KEYDOWN as KD, MOUSEBUTTONDOWN as MD, KEYUP as KU


pygame.init()
window = dis.set_mode((500,500))
dis.set_caption("i just wanna find that frikin sprite location")
pygame.key.set_repeat(40)

black = (0,0,0)
white = (255,255,255)

pixelSize = 16
imageToLocate = pygame.image.load("assets/sprites/player.png")
ITLSize = imageToLocate.get_size()
imageToLocate = pygame.transform.scale(imageToLocate, (ITLSize[0]*pixelSize, ITLSize[1]*pixelSize))
xPosFix = 0
YPosFix = 0
mouseStartPos = 0
isMoveImage = False
moving_speed = 5

while True:
    is_ctr_pressed = pygame.key.get_pressed()[pygame.K_LCTRL] + 1
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif ev.type == KD:
            if ev.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif ev.key == pygame.K_SPACE:
                isMoveImage = True
            elif ev.key == pygame.K_LEFT:
                xPosFix -= moving_speed*is_ctr_pressed
            elif ev.key == pygame.K_RIGHT:
                xPosFix += moving_speed*is_ctr_pressed
            elif ev.key == pygame.K_UP:
                YPosFix -= moving_speed*is_ctr_pressed
            elif ev.key == pygame.K_DOWN:
                YPosFix += moving_speed*is_ctr_pressed
        elif ev.type == KU:
            if ev.key == pygame.K_SPACE:
                isMoveImage = False
        elif ev.type == MD:
            print ("x_pos: ", end="")
            print (int((ev.pos[0] - xPosFix)/pixelSize), end=", ")
            print ("y_pos: ", end="")
            print (int((ev.pos[1] - YPosFix)/pixelSize))

    mousePosition = pygame.mouse.get_pos()
    if isMoveImage:
        posToRender = (xPosFix + mousePosition[0] - mousePosition[0], YPosFix + mousePosition[1] - mouseStartPos[1])
    else:
        posToRender = (xPosFix, YPosFix)
        mouseStartPos = mousePosition

    window.fill(white)
    window.blit(imageToLocate, posToRender)
    dis.update()