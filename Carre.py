class Carre():
    def __init__(self,parent):
        self.parent=parent
        self.x1=280
        self.x2=320
        self.y1=280
        self.y2=320

    def bouge(self,x,y):
        self.x1=x-20
        self.x2=x+20
        self.y1=y-20
        self.y2=y+20