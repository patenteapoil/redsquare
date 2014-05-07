from Carre import *
from Rectangle import *


class Modele():
    def __init__(self,parent):
        self.parent=parent
        self.rectangles=[]
        self.carre=Carre(self)
        self.creerRectangles()

    def creerRectangles(self,n=4):
        for i in range(n):
            x=random.randrange(350)+50
            y=random.randrange(350)+50
            self.rectangles.append(Rectangle(self,x,y))
    def miseajour(self):
        for i in self.rectangles:
            i.bouge()
    def bougerCarre(self,x,y):
        self.carre.bouger(x,y)
