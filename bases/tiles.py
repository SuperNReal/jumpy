from pygame import Rect, image, transform, Surface, draw


class Tiles():
    def __init__(self, name, size_rect, size_tile):
        tilesFolder = "assets/tiles/"
        tilesFileName = {
            "grass":"grass.png"
        }

        tileImage = image.load(tilesFolder + tilesFileName[name])
        tileImage = transform.scale(tileImage, size_rect)
        tileRect = tileImage.get_rect()
        tileSurface = Surface(size_tile)
        tileSurfaceRect = tileSurface.get_rect()
        tileRepeat = int(tileSurfaceRect.w / tileRect.w)
        tileXPos = 0
        for tileIndex in range(tileRepeat):
            tileSurface.blit(tileImage, (tileXPos, 0))
            tileXPos += tileRect.w
        self.tile = tileSurface
    
    
    def set_tile(self):
        pass

    
    def render(self, surface:Surface, position):
        surface.blit(self.tile, position)

        rect = self.tile.get_rect()
        rect.x, rect.y = position

        draw.rect(surface, (0,0,0), rect, 1)