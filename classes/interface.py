import json

from pygame import Surface

from gui.elements.button import Button
from gui.elements.text import Text
from gui.elements.rect import Rectangle


class Interface():
    def __init__(self, surface_size:tuple, interface_file:str):
        self.surface_size = surface_size
        self.file = json.load(open(interface_file))
        settings = self.file["settings"]
        self.font = settings["font"]

        self.elements = {
            "rects": {},
            "texts": {},
            "buttons": {}
        }
    
    def load_interface(self, name:str):
        self.elements["texts"].clear()
        self.elements["buttons"].clear()
        self.elements["rects"].clear()


        for text_name in self.file[name]["texts"].keys():
            text_info = self.file[name]["texts"][text_name]
            text_obj = Text(self.font, *text_info)
            self.elements["texts"][text_name] = text_obj
        
        for btn_name in self.file[name]["buttons"].keys():
            btn_info = self.file[name]["buttons"][btn_name]
            btn_obj = Button(self.font, *btn_info)
            self.elements["buttons"][btn_name] = btn_obj
        
        for rect_name in self.file[name]["rects"].keys():
            rect_info = self.file[name]["rects"][rect_name]
            rect_obj = Rectangle(*rect_info)
            self.elements["rects"][rect_name] = rect_obj
    

    def get_text(self, name:str):
        return self.elements["texts"][name]

    def get_btn(self, name:str):
        return self.elements["buttons"][name]

    def get_rectangle(self, name:str):
        return self.elements["rects"][name]
    

    def update(self):
        for btn_name in self.elements["buttons"].keys():
            self.elements["buttons"][btn_name].update()

    def render(self, surface:Surface):
        for element_name in self.elements.keys():
            for obj_name in self.elements[element_name].keys():
                self.elements[element_name][obj_name].render(surface)