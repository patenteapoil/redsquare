from tkinter import *
import random

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self.carreBouge=0
        self.canevas=Canvas(self.root,width=450,height=450,bg="black")
        self.canevas.pack()

        self.canevas.bind("<Button-1>",self.clic)
        self.canevas.bind("<ButtonRelease>",self.pasDeClic)
        self.canevas.bind("<Motion>",self.bouge)

         
    def bouge(self,evt):
        if self.carreBouge:
            self.parent.bougerCarre(evt.x,evt.y)
        
    def clic(self,evt):
        lestags=self.canevas.gettags("current")
        if "carre" in lestags:
            self.carreBouge=1
        elif "jouer" in lestags:
            self.parent.jouer()
        elif "scores" in lestags:
            self.parent.highScores()
        elif "quitter" in lestags:
            self.parent.quitter()

            
    def pasDeClic(self,evt):
        self.carreBouge=0
        
    def miseajour(self,modele):
        self.canevas.delete(ALL)
        self.canevas.create_rectangle(50,50,400,400, fill="white")
        for i in modele.rectangles:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2,fill="blue", tags=("rectangle"))
        j=modele.carre
        self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="yellow", tags=("carre"))

    def menuPrincipal(self):
        self.canevas.delete(ALL)


    def quitter(self):
        self.parent.quitter()




        

            

        
        
        
        
        
        
        
        
        
        
        
        