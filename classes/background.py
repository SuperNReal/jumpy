from pygame import font, image, Surface
from random import randint, choice
from os import path

from objects.cloud import Cloud
from gui.other.colors import Colors


class Background():
    def __init__(self, dir_assets:str, cloud_rows:int, cloud_columns:int, cloud_gab:int, reset_point:int):
        self.directory = dir_assets
        self.image = image.load(path.join(self.directory, "sprites", "background.png"))

        self.clouds = []
        for cloud_row in range(cloud_rows):
            for cloud_column in range(cloud_columns):
                pos_x = randint(-20, 40) + cloud_row*cloud_gab
                pos_y = randint(-40, 40) + cloud_column*cloud_gab
                self.clouds.append(Cloud((pos_x, pos_y), path.join(self.directory, "sprites", "cloud.png"), reset_point))


    def update(self):
        for cloud in self.clouds:
            cloud.update()
    

    def render(self, surface:Surface, offset):
        cloud_offset = offset/60
        image_offset = offset/30

        i = self.image.get_rect()
        s = surface.get_rect()
        

        for cloud in self.clouds:
            cloud.render(surface, cloud_offset)

        surface.blit(self.image, (
            s.w - i.w,
            s.h - i.h + image_offset
            ))