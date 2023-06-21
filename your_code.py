import pygame
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((800, 600))
Color = pygame.Color(102, 255, 178)
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Platformzz")
score = 0
level = 1
required_score = 0
character_image_right = pygame.image.load("assets/sprites/old_player.png")
character_rect = character_image_right.get_rect()
character_rect.topleft = (350, 550)

def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)

class Platform:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def show_intro_screen():
    intro_text = font.render("Welcome to the Platformer Game!", True, (255, 255, 255))
    instructions_text = font.render("Use arrow keys to move and spacebar to jump.", True, (255, 255, 255))
    intro_button_text = font.render("Start Game", True, (255, 255, 255))
    intro_button_rect = pygame.Rect(335, 500, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if intro_button_rect.collidepoint(event.pos):
                    return "game"
                    break

        win.fill(Color)
        win.blit(intro_text, (200, 200))
        win.blit(instructions_text, (150, 250))
        pygame.draw.rect(win, (255, 0, 0), intro_button_rect)
        win.blit(intro_button_text, (345, 515))
        pygame.display.flip()

def show_win_screen():
    global score
    win_text = font.render(f"Congratulations! You Win! Score: {score}", True, (255 ,255 ,255))
    win_button_text = font.render("Replay Game", True, (255, 255, 255))
    win_button_rect = pygame.Rect(320, 500, 175, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if win_button_rect.collidepoint(event.pos):
                    return "intro"
                    break

        win.fill(Color)
        win.blit(win_text, (180, 200))
        pygame.draw.rect(win, (255, 0, 0), win_button_rect)
        win.blit(win_button_text, (330, 515))
        pygame.display.flip()

def show_game_over_screen():
    game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 255, 255))
    game_over_button_text = font.render("Replay Level", True, (255, 255, 255))
    game_over_button_rect = pygame.Rect(350, 500, 150, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game_over_button_rect.collidepoint(event.pos):
                    return "level"
                    break

        win.fill(Color)
        win.blit(game_over_text, (280, 200))
        pygame.draw.rect(win, (255, 0, 0), game_over_button_rect)
        win.blit(game_over_button_text, (360, 515))
        pygame.display.flip()

def show_next_level_screen():
    global score
    next_level_text = font.render(f"Congrats! You can move on to the next level! Score: {score}", True, (255, 255, 255))
    next_level_button_text = font.render("Next Level", True, (255, 255, 255))
    next_level_button_rect = pygame.Rect(350, 500, 150, 50)
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if next_level_button_rect.collidepoint(event.pos):
                    return "next_level"
                    break
                    

        win.fill(Color)
        win.blit(next_level_text, (280, 200))
        pygame.draw.rect(win, (255, 0, 0), next_level_button_rect)
        win.blit(next_level_button_text, (360, 515))
        pygame.display.flip()
        pass
    
def initialize_level():
    global level, required_score
    platforms = []

    if level == 1:
        platform1 = Platform(200, 400, 100, 20, (0, 255, 0))
        platform2 = Platform(300, 200, 100, 20, (0, 255, 0))
        platform3 = Platform(100, 100, 100, 20, (0, 255, 0))
        platform4 = Platform(400, 400, 100, 20, (0, 255, 0))
        platform5 = Platform(600, 500, 100, 20, (0, 255, 0))
        platform6 = Platform(600, 750, 100, 20, (0, 255, 0))
        platforms = [platform1, platform2, platform3, platform4, platform5, platform6]
        required_score = 560
        
    elif level == 2:
        platform1 = Platform(400, 400, 100, 20, (0, 255, 0))
        platform2 = Platform(600, 500, 100, 20, (0, 255, 0))
        platforms = [platform1, platform2]
        required_score = 400
        
    elif level == 3:
        platform1 = Platform(600, 750, 100, 20, (0, 255, 0))
        platforms = [platform1]
        required_score = 500

    return platforms, required_score

def play_level():
    global score, character_rect, level, required_score
    # character_image_left = pygame.image.load("marioLeft.png")
    # character_running_image = pygame.image.load("marioRunning.gif")

    character_speed = 1
    gravity = 1
    jump_force = 20
    is_jumping = False
    velocity = jump_force

    platforms, required_score = initialize_level()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif score >= required_score:
                if level == 3:
                    return "win"
                else:
                    return "next_level"
            

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # character_image = character_running_image
            # character_image = pygame.transform.flip(character_image, True, False)
            # character_image = pygame.transform.scale(character_image, (50, 50))
            character_rect.x -= character_speed
        elif keys[pygame.K_RIGHT]:
            # character_image = character_running_image
            # character_image = pygame.transform.flip(character_image, False, False)
            # character_image = pygame.transform.scale(character_image, (50, 50))
            character_rect.x += character_speed
        elif keys[pygame.K_SPACE]:
            is_jumping = True
       
        else:
            character_image = character_image_right

        if is_jumping:
            pygame.time.delay(30)
            character_rect.y -= velocity
            velocity -= gravity
            if keys[pygame.K_LEFT]:
                character_rect.x -= character_speed + 10
            elif keys[pygame.K_RIGHT]:
                character_rect.x += character_speed + 10
            if velocity < -jump_force:
                is_jumping = False
                velocity = jump_force

        on_ground = False
        for platform in platforms:
            if character_rect.colliderect(platform.rect):
                if velocity >= 0:
                    character_rect.y = platform.rect.y - character_rect.height
                    is_jumping = False
                    velocity = jump_force
                    on_ground = True
                else:
                    character_rect.y += velocity
       

        if on_ground == False:
            character_rect.y += gravity

        if character_rect.y < 200:
            for platform in platforms:
                platform.rect.y += gravity

        character_rect.x = clamp(character_rect.x, 0, win.get_width() - character_rect.width)
        character_rect.y = clamp(character_rect.y, 0, win.get_height() - character_rect.height)

        win.fill(Color)
        win.blit(character_image_right, character_rect)
        for platform in platforms:
            platform.draw(win)
        score = max(score, 600 - character_rect.y)  
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        win.blit(score_text, (10, 10))
        pygame.display.flip()



current_screen = "intro"
game_running = True
while game_running:
    if current_screen == "intro":
        current_screen = show_intro_screen()
    elif current_screen == "game":
        result = play_level()
        if result == "win":
            current_screen = show_win_screen()
        elif result == "next_level":
            level += 1
            current_screen = show_next_level_screen()
        else:
            current_screen = show_game_over_screen()


pygame.quit()