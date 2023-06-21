from pygame import Rect, Surface
from os import path

from objects.platform import Platform


class Levels():
    def __init__(self, levels_dir:str, block_size=40):
        self.directory = levels_dir
        self.block_size = block_size
        self.level_data = {}
        self.level_objects = {}
    
    def load_level(self, level_num:int):
        self.level_data.clear()
        self.level_objects.clear()


        level_lines = None

        with open(path.join(self.directory, "level_"+str(level_num)+".txt")) as level_file:
            level_lines = level_file.readlines()
        
        self.level_data["rect"] = Rect(0,0,
            (len(level_lines[0])-1)*self.block_size,
            len(level_lines)*self.block_size
            )


        platf_pos = None
        platf_width = 1
        index_row = 0
        for level_line in level_lines:
            index_column = 0
            for level_letter in level_line:
                block_pos = (
                    self.block_size*index_column,
                    self.block_size*index_row
                )
                level_obj = None


                match level_letter:
                    case "P":
                        self.level_data["spawn"] = block_pos
                    case "S":
                        platf_pos = block_pos
                        platf_width = 1
                    case "I":
                        platf_width += 1
                    case "F":
                        platf_width += 1
                        level_obj = Platform(platf_pos, ( self.block_size*platf_width, self.block_size))
                
                if not level_obj is None:
                    obj_name = level_obj.get_name()
                    while True:
                        try:
                            self.level_objects[obj_name].append(level_obj)
                            break
                        except KeyError:
                            self.level_objects[obj_name] = []


                index_column += 1
            index_row += 1
    

    def get_level_rect(self):
        return self["rect"]
    
    def get_level_data(self, data_name):
        return self.level_data[data_name]
    
    def get_level_objects(self):
        return self.level_objects


    def render(self, surface:Surface):
        for name in self.level_objects:
            for level_obj in self.level_objects[name]:
                level_obj.render(surface)