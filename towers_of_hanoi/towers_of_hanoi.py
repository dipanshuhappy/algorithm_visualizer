from graphics import *
import sys
win=GraphWin(title='towers of hanoi',width=800,height=800)
class Tower:
    def __init__(self,id,point,discs=[]):
        self.id=id
        self.point:Point=point
        self.discs:list=discs
        self.tower:Rectangle=Rectangle(point,Point(point.x+30,point.y+400))
    def draw_tower(self):
        self.tower.setFill('blue')
        self.tower.draw(win)
    def undraw_tower(self):
        self.tower.undraw()
class Disc:
    def __init__(self,value:int,color:str,point:Point,dimension:tuple):
        self.value=value
        self.color=color
        self.point=point
        self.dimension=dimension
        self.disc=Rectangle(point,Point(point.x+dimension[0],point.y+dimension[1]))
    def draw_disc(self):
        self.disc.setFill(self.color)
        self.disc.draw(win)
    def move_disc(self,tower:Tower):
        tower.undraw_tower()
        print('animating')
        dx=tower.tower.getP2().x-self.disc.getCenter().x
        dy=tower.tower.getP2().y-self.disc.getCenter().y
        if len(tower.discs)>0:
            dy=dy-(self.dimension[1]*len(tower.discs))
        
        self.disc.move(dx,dy)
        tower.draw_tower()

class Towers:
    def __init__(self, towers,rings=3):
        self.rings=rings
        self.towers=towers
        self.towers[0].discs=self.initialize_discs()
        self.towers[1].discs=[]
        self.towers[2].discs=[]
   
    def initialize_discs(self):
        output=[
            Disc(value=3,color='red',point=Point(65,550),dimension=(200,20)),
            Disc(value=2,color='cyan',point=Point(88,515),dimension=(150,20)),
            Disc(value=1,color='green',point=Point(115,480),dimension=(100,20))
        ]
        return output
    def __str__(self):
        outcm=""
        for i in range(self.rings,-1, -1):
            for j in range(3):
                if len(self.towers[j].discs)>i:
                    outcm +=" " +str(self.towers[j].discs[i].value)
                else:
                    outcm +="  "
            outcm += "\n"
        return outcm + "-------"  

    def move(self,front_tower, dest_tower):
        ring=self.towers[front_tower].discs.pop()
        time.sleep(1)
        ring.move_disc(self.towers[dest_tower])
        self.towers[dest_tower].discs.append(ring)
       

def solve_tower_of_hanoi(towers, n, star_tower, dest_tower, aux_tower):
    if n==0:
        return 

    solve_tower_of_hanoi(towers, n-1, star_tower, aux_tower, dest_tower)

    towers.move(star_tower, dest_tower)
    print(towers)

    solve_tower_of_hanoi(towers, n-1, aux_tower, dest_tower, star_tower)
def run_towers_of_hanoi():
    output=Towers([
        Tower(1,Point(150,200)),
        Tower(2,Point(370,200)),
        Tower(3,Point(600,200)),
    ])
    for tower in output.towers:
        tower.draw_tower()
        if len(tower.discs)>0:
            for disc in tower.discs:
                disc.draw_disc()
    solve_tower_of_hanoi(output, output.rings, 0, 2, 1)
    win.getMouse()
    win.close()
    sys.exit()
run_towers_of_hanoi()
# print(output)

