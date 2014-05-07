from Modele import *
from Vue import *

class Controleur():
    def __init__(self):
        self.actif=1
        self.modele=Modele(self)
        self.vue=Vue(self)
        self.jouer()
        self.vue.root.mainloop()

    def bougerCarre(self,x,y):
        self.modele.bougerCarre(x,y)

    def jouer(self):
        if self.actif:
            self.modele.miseajour()
            self.vue.miseajour(self.modele)
            self.vue.root.after(50,self.jouer)

    def demarrer(self):
        self.vue.menuPrincipal()

    def highScores(self):
        self.modele.highScores()

    def quitter(self):
        self.vue.root.destroy()
if __name__ == '__main__':
    c=Controleur()