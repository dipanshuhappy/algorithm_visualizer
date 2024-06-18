  def __init__(self,value:int,color:str,point:Point,dimension:tuple):
        self.value=value
        self.color=color
        self.point=point
        self.dimension=dimension
        self.disc=Rectangle(point,Point(point.x+dimension[0],point.y+dimension[1]))
