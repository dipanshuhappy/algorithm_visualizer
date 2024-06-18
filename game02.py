 def __init__(self,id,point,discs=[]):
        self.id=id
        self.point:Point=point
        self.discs:list=discs
        self.tower:Rectangle=Rectangle(point,Point(point.x+30,point.y+400))
