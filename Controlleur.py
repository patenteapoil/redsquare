from Modele import *
from Vue import *

class Controleur():
    def __init__(self):
        self.actif=1
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.vue.miseajour(self.modele)
        self.gameOn()
        self.vue.root.mainloop()

    def carrebouge(self,x,y):
        self.modele.carre.bouge(x,y)

    def gameOn(self):
        if self.actif:
            self.modele.miseajour()
            self.vue.miseajour(self.modele)
            self.vue.root.after(50,self.gameOn)

if __name__ == '__main__':
    c=Controleur()