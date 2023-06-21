from pygame import Rect, Surface, draw


class Eyes():
    def __init__(self, parent, size:tuple, color:tuple):
        self.size = size
        self.color = color
        self.parent = parent

        self.state_move = 1
        self.state_hurt = 2
        self.state_disappointed = 3
        self.state_happy = 4
        self.cur_state = self.state_move


    def set_state(self, state:int):
        self.cur_state = state

    
    def get_rect(self):
        return Rect(self.get_position(0), self.size), Rect(self.get_position(1), self.size)

    def get_position(self, is_eye_right:bool):
        parent_rect = self.parent.get_rect()


        eye_right_fix = int(is_eye_right)*19

        if self.parent.force_x > 0:
            per_value = -self.parent.force_min_x
        else:
            per_value = self.parent.force_max_x
        eye_move_x = self.parent.force_x/per_value*2.5

        if self.parent.force_y > 0:
            per_value = -self.parent.force_min_y - 12
        else:
            per_value = self.parent.force_max_y
        eye_move_y = self.parent.force_y/per_value*4

        pos = (parent_rect.x + 13 + eye_right_fix + eye_move_x, parent_rect.y + 14 + eye_move_y)

        return pos

    def get_lines_hurt(self):
        parent_rect = self.parent.get_rect()
        eye_right_fix = 19

        line = [
            [parent_rect.x + 12, parent_rect.y + 13],
            [parent_rect.x + 18, parent_rect.y + 19]
        ]

        line2  = [
            [line[1][0] + eye_right_fix, line[0][1]],
            [line[0][0] + eye_right_fix, line[1][1]]
        ]

        return line, line2

    def get_line_disappointed(self):
        parent_rect = self.parent.get_rect()
        eye_right_fix = 19

        line = (
            [parent_rect.x + 11, parent_rect.y + 16],
            [parent_rect.x + 19, parent_rect.y + 16]
        )

        line2 = (
            [line[1][0] + eye_right_fix, line[1][1]],
            [line[0][0] + eye_right_fix, line[0][1]]
        )

        return line, line2

    def get_lines_happy(self, is_flip:bool):
        parent_rect = self.parent.get_rect()
        eye_right_fix = 19
        line_list = []

        end_x = 15
        if is_flip:
            start_y = 20
            end_y = 12
        else:
            start_y = 12
            end_y = 20

        lines = [
            ( [11, start_y], [end_x, end_y] ),
            ( [19, start_y], [end_x, end_y] )
        ]
        lines2 = [
            ( [11+eye_right_fix, start_y], [end_x+eye_right_fix, end_y] ),
            ( [19+eye_right_fix, start_y], [end_x+eye_right_fix, end_y] )
        ]

        for line_list in [lines, lines2]:
            for line in line_list:
                for point in line:
                    point[0] += parent_rect.x
                    point[1] += parent_rect.y

        return lines, lines2
    

    def render(self, surface:Surface):
        if self.cur_state == self.state_move:
            for rect in self.get_rect():
                draw.rect(surface, self.color, rect)

        elif self.cur_state == self.state_hurt:
            for line in self.get_lines_hurt():
                draw.line(surface, (0,0,0), *line, 3)
        
        elif self.cur_state == self.state_disappointed:
            for line in self.get_line_disappointed():
                draw.line(surface, (0,0,0), *line)
            
        elif self.cur_state == self.state_happy:
            for line_list in self.get_lines_happy(1):
                draw.line(surface, (0,0,0), *line_list[0])
                draw.line(surface, (0,0,0), *line_list[1])