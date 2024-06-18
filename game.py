 def __init__(self,window_dimension):
        self.screen=pygame.display.set_mode(window_dimension)
        self.width=window_dimension[0]
        self.height=window_dimension[1]
        self.initialize_grid()
