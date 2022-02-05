class Towers:
    def __init__(self, rings=3):
        self.rings=rings
        self.towers=[[]]*3
        self.towers[0]=[i for i in range(self.rings,0,-1)]
        self.towers[1]=[]
        self.towers[2]=[]
        

    def __str__(self):
        outcm=""
        for i in range(self.rings,-1, -1):
            for j in range(3):
                if len(self.towers[j])>i:
                    outcm +=" " +str(self.towers[j][i])
                else:
                    outcm +="  "
            outcm += "\n"
        return outcm + "-------"  

    def move(self,front_tower, dest_tower):
        ring=self.towers[front_tower].pop()
        self.towers[dest_tower].append(ring)
       

def solve_tower_of_hanoi(towers, n, star_tower, dest_tower, aux_tower):
    if n==0:
        return 

    solve_tower_of_hanoi(towers, n-1, star_tower, aux_tower, dest_tower)

    towers.move(star_tower, dest_tower)
    print(towers)

    solve_tower_of_hanoi(towers, n-1, aux_tower, dest_tower, star_tower)

output=Towers(5)
print(output)
solve_tower_of_hanoi(output, output.rings, 0, 2, 1)



