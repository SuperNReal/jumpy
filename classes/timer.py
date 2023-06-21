class Timer():
    def __init__(self):
        self.__reset_timer()

    def __reset_timer(self):
        self.time_start = 0
        self.time_finish = 0

    
    def start(self):
        self.__reset_timer()
    
    def get(self, fps:float):
        return (self.time_finish - self.time_start)/fps

    def update(self):
        self.time_finish += 1