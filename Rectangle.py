import random

class Rectangle():
    def __init__(self,parent,x,y):
        self.parent=parent
        self.x1=x-10
        self.x2=x+10
        self.y1=y-10
        self.y2=y+10
    def bouge(self,x=10,y=10):
        xa=random.randrange(x)*(random.randrange(3)-1)
        ya=random.randrange(x)*(random.randrange(3)-1)
        self.x1=self.x1+xa
        self.x2=self.x2+xa
        self.y1=self.y1+xa
        self.y2=self.y2+xa
