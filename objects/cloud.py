from pygame import image, transform, Surface


class Cloud():
    def __init__(self, position:tuple, image_path:str, reset_point:int, speed_move=0.5):
        self.image = image.load(image_path)
        self.image_width = self.image.get_width()
        self.pos_x, self.pos_y = position
        self.speed_move = speed_move
        self.reset_point = reset_point
    

    def update(self):
        self.pos_x += self.speed_move
        if self.pos_x >= self.reset_point:
            self.pos_x = -self.image_width
    

    def render(self, surface:Surface, pos_y_offset:int):
        surface.blit(self.image, (self.pos_x, self.pos_y+pos_y_offset))