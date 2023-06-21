class Entity():
    def __init__(self):
        self.force_x = 0
        self.force_y = 0
        self.force_max_x = 5
        self.force_min_x = -7.5
        self.force_max_y = 9
        self.force_min_y = -21
        self.force_speed_x = 0.4
        self.force_speed_y = 0.6


    def get_force(self):
        return self.force_x, self.force_y

    def add_force(self, value_x:int, value_y:int):
        outcome_force_x = self.force_x + value_x
        outcome_force_y = self.force_y + value_y

        if self.force_max_x < outcome_force_x:
            self.force_x = self.force_max_x
        if self.force_min_x > outcome_force_x:
            self.force_x = self.force_min_x
        else:
            self.force_x += value_x
        
        if self.force_max_y < outcome_force_y:
            self.force_y = self.force_max_y
        if self.force_min_y > outcome_force_y:
            self.force_y = self.force_min_y
        else:
            self.force_y += value_y

    
    def update_force_y(self):
        self.pos_y += self.force_y

        if self.force_max_y > self.force_y:
            self.force_y += self.force_speed_y
    
    def update_force_x(self):
        self.pos_x += self.force_x

        if self.force_x - self.force_speed_x > 0:
            self.force_x -= self.force_speed_x
        elif self.force_x + self.force_speed_x < 0:
            self.force_x += self.force_speed_x
        else:
            self.force_x = 0