import threading
import pygame

from pygame import display as dis, KEYDOWN as KD


is_running = True
gif_scale = 5
gif_image = pygame.image.load("assets/gifs/face_wink.gif")
gif_image = pygame.transform.scale_by(gif_image, gif_scale)


pygame.init()
window = dis.set_mode(gif_image.get_size())
dis.set_caption("why not you stupid bas#@%#")

def kill():
    is_running = False

def try_sup_thread():
    window.fill("white")
    window.blit(gif_image, (0,0))
    dis.update()

gif_thread = threading.Thread(target=try_sup_thread)
gif_thread.daemon = True
while is_running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            kill()
            break
        elif ev.type == KD:
            if ev.key == pygame.K_ESCAPE:
                kill()
                break
            elif ev.key == pygame.K_SPACE:
                gif_thread.start()
    
    # window.fill("white")
    # window.blit(gif_image, (0,0))
    # dis.update()
            



pygame.quit()