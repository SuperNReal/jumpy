from pygame import Rect, image, Surface, draw

from bases.tiles import Tiles
from gui.other.colors import Colors


class Platform():
    def __init__(self, position:tuple, size:tuple):
        self.pos = position
        self.size = size
        self.tile = Tiles("grass", (40, 40), size)
    

    def get_name(self):
        return "platforms"

    def get_rect(self):
        return Rect(self.pos, self.size)


    def render(self, surface:Surface):
        # draw.rect(surface, Colors.brown, self.get_rect())
        self.tile.render(surface, self.pos)