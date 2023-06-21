import pygame
import json

from pygame import Rect, key, Surface, image, transform, draw
from os import path

from classes.collistion import Collistion
from classes.player_eyes import Eyes
from gui.other.colors import Colors
from bases.entity import Entity


class Player(Entity):
    def __init__(self, size:tuple, camera_size:tuple, dir_sprites, spawn:tuple, speed_move=5, speed_jump=13):
        super().__init__()
        self.size = size
        self.camera_size = camera_size
        self.directory = dir_sprites
        self.color = Colors.green
        self.pos_x, self.pos_y = spawn
        self.speed_move = speed_move
        self.speed_jump = -speed_jump

        self.input_config = json.load(open("config/key_bind.json"))
        self.sprite = image.load(path.join(self.directory, "sprites", "player.png"))
        self.sprite = transform.scale(self.sprite, size)
        self.eyes = Eyes(self, (5, 5), Colors.blue)

        self.is_on_wall_left = False
        self.is_on_wall_right = False
        self.is_on_ground = False
    
    def teleport(self, x:int, y:int):
        self.pos_x = x
        self.pos_y = y
    
    def move(self, x:int, y:int):
        self.pos_x += x
        self.pos_y += y
    
    def __get_value_of_key(self, key_name):
        return getattr(pygame, "K_" + key_name)
    
    def __pos_fix(self):
        self.pos_x = max(0, min( self.pos_x, self.camera_size[0] - self.size[0] ))
    
    def __jump(self):
        if self.is_on_ground:
            self.add_force(0, self.speed_jump)
            self.is_on_ground = False
        
    def __collide_eyes(self, collide_side:str):
        if collide_side == "up":
            self.eyes.set_state(self.eyes.state_hurt)
        elif collide_side == "down":
            self.eyes.set_state(self.eyes.state_move)
    
    def __collide_psychics(self, collide_side:str):
        if collide_side == "up":
            self.force_y = 0
    

    def get_render_position(self, parent:Surface):
        cam_width, cam_height = self.camera_size
        parent_width, parent_height = parent.get_rect().size

        render_pos_x = max(0, min(self.pos_x - cam_width/2, parent_width - cam_width) )
        render_pos_y = max(0, min(self.pos_y - cam_height/2, parent_height - cam_height) )

        return render_pos_x, render_pos_y


    def get_rect(self):
        return Rect( (self.pos_x, self.pos_y), self.size )


    def process_event(self, ev:pygame.event.EventType):
        key_jump = self.__get_value_of_key(self.input_config["jump"])
        

        if ev.type == pygame.KEYDOWN:
            if ev.key == key_jump:
                self.__jump()

    
    def update(self, *level_objects):
        if self.is_on_ground:
            self.force_y = 0
        else:
            self.update_force_y()

        if not(self.is_on_wall_left or self.is_on_wall_right):
            self.update_force_x()        


        self.__update_collision(*[level_object.get_rect() for level_object in level_objects])
        self.__update_input_keyboard()
        self.__pos_fix()
        
    def __update_collision(self, *targets:Rect):
        is_on_wall_left = False
        is_on_wall_right = False
        is_on_ground = False
        
        self_rect = self.get_rect()
        for target in targets:
            collide_side, pos_x_fix, pos_y_fix = Collistion.checkCollistion(self_rect, target, self.force_x, self.force_y)
            self.__collide_eyes(collide_side)
            self.__collide_psychics(collide_side)

            if collide_side == "down":
                is_on_ground = True
            elif collide_side == "left":
                is_on_wall_left = True
            elif collide_side == "right":
                is_on_wall_right = True
            
            if pos_x_fix != 0 and (self.is_on_wall_left or self.is_on_wall_right):
                self.teleport(pos_x_fix, self.pos_y)
            if pos_y_fix != 0 and self.is_on_ground:
                self.teleport(self.pos_x, pos_y_fix)
            
            if is_on_wall_left and is_on_wall_right and is_on_ground:
                break

        
        self.is_on_wall_left = is_on_wall_left
        self.is_on_wall_right = is_on_wall_right
        self.is_on_ground = is_on_ground
    
    def __update_input_keyboard(self):
        key_left = self.__get_value_of_key(self.input_config["left"])
        key_right = self.__get_value_of_key(self.input_config["right"])

        keys_pressed = key.get_pressed()


        if keys_pressed[key_left] and not self.is_on_wall_left:
            self.add_force(-self.speed_move, 0)
        
        if keys_pressed[key_right] and not self.is_on_wall_right:
            self.add_force(self.speed_move, 0)
                
    
    def render(self, surface:Surface):
        draw.rect(surface, self.color, self.get_rect())
        surface.blit(self.sprite, (self.pos_x, self.pos_y))
        self.eyes.render(surface)
    
    def render_camera(self, surface:Surface, parent:Surface):
        cam_width, cam_height = self.camera_size

        cam_surface = parent.subsurface(Rect(*self.get_render_position(parent), cam_width, cam_height))
        surface.blit(cam_surface, (0,0))