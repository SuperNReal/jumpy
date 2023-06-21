import pygame


pygame.mixer.init()


sample = pygame.mixer.Sound("assets/sfx/jump.mp3")
channels = [pygame.mixer.Channel(index) for index in range(2)]


while True:
    input_channel = int(input("channel number:  "))
    input_is_play = bool(int(input("is play:  ")))

    if input_is_play:
        channels[input_channel].play(sample, 4)
    else:
        channels[input_channel].stop()