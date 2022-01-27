import random
import sys
import pygame
pygame.init()
alive_color = (255,51,51)
black=(0,0,0)
def get(l,v,d):
    try:
        return l[v]
    except:
        return d
class Game:
    CELL_SIZE=10
    def __init__(self,window_dimension):
        self.screen=pygame.display.set_mode(window_dimension)
        self.width=window_dimension[0]
        self.height=window_dimension[1]
        self.initialize_grid()
    def get_random_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                self.grids[self.active][r][c]=random.choices([1,0],weights=(40,60))[0]
    def initialize_grid(self): 
        self.rows=int(self.width/Game.CELL_SIZE)             
        self.cols=int(self.height/Game.CELL_SIZE)     
        self.active=0
        # self.grids=[[[0]*self.rows]*self.cols,[[0]*self.rows]*self.cols]
        self.grids=[[[0]*self.cols for n in range(self.rows)],[[0]*self.cols for n in range(self.rows)]]        

    def get(self,a,b):
            try:
                return self.grids[self.active][a][b]
            except:
                return 0
    def reset_screen(self):
        self.screen.fill(black)
    def check_surrounding_cells(self,r,c):
        alive_around=0
        alive_around+=self.get(r+1,c+1)
        alive_around+=self.get(r+1,c)
        alive_around+=self.get(r+1,c-1)
        alive_around+=self.get(r,c+1)
        alive_around+=self.get(r,c-1)
        alive_around+=self.get(r-1,c+1)
        alive_around+=self.get(r-1,c)
        alive_around+=self.get(r-1,c-1)
        cell=self.grids[self.active][r][c]
        if cell==1:
            if alive_around>3:
                return 0
            elif alive_around<2:
                return 0
            elif alive_around==2 or alive_around==3:
                return 1
        else:
            if alive_around==3:
                return 1
        return 0

    def update_screen(self):
        for r in range(self.rows):
            for c in range(self.cols):
                next_state=self.check_surrounding_cells(r,c)
                self.grids[(self.active+1)%2][r][c]=next_state
        self.active=(self.active+1)%2
    def draw_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                x=int(r*Game.CELL_SIZE+Game.CELL_SIZE/2)
                y=int(c*Game.CELL_SIZE+Game.CELL_SIZE/2)
                if self.grids[self.active][r][c]==1:
                    ran_int=random.choice([1,2,3])
                    if ran_int==1:
                        pygame.draw.circle(self.screen,alive_color,(x,y),Game.CELL_SIZE/2)
                    elif ran_int==2:
                        pygame.draw.circle(self.screen,(0,255,0),(x,y),Game.CELL_SIZE/2)
                    else:
                        pygame.draw.circle(self.screen,(0,0,255),(x,y),Game.CELL_SIZE/2)
                    # pygame.draw.circle(self.screen,alive_color,(x,y),Game.CELL_SIZE/2)
                else:
                    pygame.draw.circle(self.screen,black,(x,y),Game.CELL_SIZE/2)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_r:

                    self.get_random_grid()
                    self.draw_grid()
    def run_mainloop(self):
         self.reset_screen()
         self.get_random_grid()
         self.draw_grid()
         while True:
            #  pygame.time.Clock().tick(100)
             self.handle_events()
             self.update_screen()
             self.draw_grid()
            #  self.get_random_grid()
             pygame.display.flip()
          
if __name__=='__main__':
    g=Game(( 1400, 800))
   
    g.run_mainloop()
    
