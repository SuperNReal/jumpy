import pygame
import sys
import os

from classes.timer import Timer
from classes.levels import Levels
from classes.background import Background
from classes.interface import Interface
from entities.player import Player


from gui.other.colors import Colors
from gui.elements.text import Text
from gui.elements.rect import Rectangle

try:
    os.chdir(getattr(sys, "_MEIPASS"))
except:
    pass


class Game():
    def __init__(self):
        pygame.init()

        # init classes
        #--------------------------------------------------------------------------------------------------
        self.cur_level = 0
        self.cur_interface = "intro"
        self.final_level_num = len(os.listdir("levels"))-1
        self.is_show_interface = True

        self.levels = Levels("levels")
        self.levels.load_level(self.cur_level)
        level_rect = self.levels.get_level_data("rect")

        camera_size = (level_rect.w, 500)

        self.interface = Interface(level_rect.size, "config/interface_file.json")
        self.interface.load_interface(self.cur_interface)

        self.background = Background("assets", 6, 2, 150, level_rect.w)
        self.main_player = Player((50,50), camera_size, "assets", self.levels.get_level_data("spawn"))
        self.timer = Timer()

        # init elements to use in render
        #--------------------------------------------------------------------------------------------------
        status_offset_y = 10

        self.dis_level_num = Text("assets/fonts/in_game.ttf", "level 0", 44, (0,0), Colors.black)
        self.dis_level_num.setParent(Rectangle(level_rect.size, (0,0)), (0,0))
        self.dis_level_num.setParentRelation("in-down")

        self.dis_timer = Text("assets/fonts/in_game.ttf", "", 21, (0,0))
        self.dis_timer.setParent(Rectangle(level_rect.size, (0,0)), ((0, -(level_rect.h - self.dis_timer.getRect(False).h)/2 + status_offset_y )))
        self.dis_timer.setParentRelation("in-left")

        self.dis_arrows = pygame.image.load("assets/sprites/arrows.png")
        self.dis_arrows = pygame.transform.scale_by(self.dis_arrows, 3)
        self.dis_arrows_pos = (280,320)

        # init display
        #--------------------------------------------------------------------------------------------------
        self.window = pygame.display.set_mode(camera_size)
        pygame.display.set_caption("some dudes game remake;)")
        pygame.display.set_icon(pygame.image.load("assets/icon.png"))
        self.clock = pygame.time.Clock()
        self.FPS = 60


        # pygame.mixer_music.load("assets/music/peaceful_forest.mp3")
        # pygame.mixer_music.play(-1)
    
    def kill(self):
        pygame.quit()
        sys.exit()
    
    def run(self):
        while True:
            self.process_events()
            self.update()
            self.render()
            self.clock.tick(self.FPS)
        
    def change_level(self, level_num:int):
        self.cur_level = level_num
        self.levels.load_level(self.cur_level)
        self.main_player.eyes.set_state(self.main_player.eyes.state_move)
        self.main_player.teleport(*self.levels.get_level_data("spawn"))
        self.dis_level_num.setParent(Rectangle(self.levels.get_level_data("rect").size, (0,0)), (0,0))
        self.dis_level_num.setText("level" + str(self.cur_level))
    
    def change_interface(self, interface_name:str):
        self.cur_interface = interface_name
        self.interface.load_interface(self.cur_interface)

    def __interface_events(self, ev:pygame.event.EventType):
        if self.is_show_interface:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.cur_interface == "intro":
                    if self.interface.get_btn("start").checkCollision(ev.pos):
                        self.change_level(1)
                        self.change_interface("level finish")
                        self.timer.start()


                elif self.cur_interface == "level finish":
                    if self.interface.get_btn("next_level").checkCollision(ev.pos):
                        if self.get_is_player_win():
                            try:
                                self.change_level(self.cur_level+1)
                            except FileNotFoundError:
                                self.change_level(0)
                                self.change_interface("intro")
                        else:
                            self.change_level(self.cur_level)
    

    def get_is_player_win(self):
        return self.main_player.get_rect().y <= 0
    
    def get_is_player_lose(self):
        rect_player = self.main_player.get_rect()
        rect_level = self.levels.get_level_data("rect")
        return rect_player.y + rect_player.h >= rect_level.h
    

    def process_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                self.kill()
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.kill()
            self.__interface_events(ev)
            self.main_player.process_event(ev)
    
    def update(self):
        if not self.is_show_interface:
            self.timer.update()
        self.background.update()
        self.main_player.update(*self.levels.get_level_objects()["platforms"])
        if self.is_show_interface:
            self.interface.update()


        if self.get_is_player_win():
            rect_bc = self.interface.get_rectangle("message_background")
            text_m = self.interface.get_text("message")
            btn_n = self.interface.get_btn("next_level")
            self.main_player.eyes.set_state(self.main_player.eyes.state_happy)

            if self.cur_level == self.final_level_num:
                rect_bc.setColor(Colors.white)
                rect_bc.setSize((380, 90))
                text_m.setFont("assets/fonts/in_game.ttf")
                text_m.setText("thx 4 playing :d, score:{timer:.2f}".format(timer = self.timer.get(self.FPS)))
                btn_n.getText().setText("click to restart")
            else:
                rect_bc.setColor(Colors.green)
                text_m.setText("nice rocks!, you win:)")
                btn_n.getText().setText("click to progress")
            self.is_show_interface = True
            # self.__change_level(self.cur_level)

        elif self.get_is_player_lose():
            rect_bc = self.interface.get_rectangle("message_background")
            text_m = self.interface.get_text("message")
            btn_n = self.interface.get_btn("next_level")
            rect_bc.setColor(Colors.red)
            text_m.setText("to bad:(, you lost:D")
            btn_n.getText().setText("click to retry")
            self.is_show_interface = True
            
        else:
            if self.cur_interface == "intro":
                self.dis_timer.setText("")
            else:
                self.is_show_interface = False
                self.dis_timer.setText("score: {timer:.2f}".format(timer = self.timer.get(self.FPS)))
    

    def render(self):
        if self.cur_level == 0:
            self.window.fill(Colors.orange)
        else:
            self.window.fill(Colors.light_blue)

        self.__render_game()

        if self.cur_interface == "intro":
            self.__render_game_controls()
        else:
            self.dis_timer.render(self.window)

        if self.is_show_interface:
            self.interface.render(self.window)
        pygame.display.update()

    def __render_game(self):
        level_rect = self.levels.get_level_data("rect")
        surface_level = pygame.Surface(level_rect.size)
        chrome_key_color = Colors.red

        self.background.render(self.window, self.levels.get_level_data("spawn")[1] - self.main_player.get_render_position(surface_level)[1] )

        surface_level.fill(chrome_key_color)
        surface_level.set_colorkey(chrome_key_color)
        self.levels.render(surface_level)
        if self.cur_interface != "intro":
            self.dis_level_num.render(surface_level)
        self.main_player.render(surface_level)
        self.main_player.render_camera(self.window, surface_level)
    
    def __render_game_controls(self):
        self.window.blit(self.dis_arrows, self.dis_arrows_pos)

        dis_left = Text("assets/fonts/in_game.ttf", self.main_player.config_key["left"], 23, (self.dis_arrows_pos[0] - 50, self.dis_arrows_pos[1] + 110))
        dis_right = Text("assets/fonts/in_game.ttf", self.main_player.config_key["right"], 23, (self.dis_arrows_pos[0] + 230, self.dis_arrows_pos[1] + 110))
        dis_jump = Text("assets/fonts/in_game.ttf", self.main_player.config_key["jump"], 23, (self.dis_arrows_pos[0] + 83, self.dis_arrows_pos[1] - 15))
        
        dis_left.render(self.window)
        dis_right.render(self.window)
        dis_jump.render(self.window)


if __name__ == "__main__":
    game = Game()
    game.run()
