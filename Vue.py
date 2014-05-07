from tkinter import *
import random

class Vue():
    def __init__(self,parent):
        self.parent=parent
        self.root=Tk()
        self.carrebouge=0
        self.canevas=Canvas(self.root,width=450,height=450,bg="black")
        self.canevas.pack()

        self.canevas.bind("<Button-1>",self.gotclick)
        self.canevas.bind("<ButtonRelease>",self.forgotclick)
        self.canevas.bind("<Motion>",self.bouge)

         
    def bouge(self,evt):
        if self.carrebouge:
            self.parent.carrebouge(evt.x,evt.y)
        
    def gotclick(self,evt):
        lestags=self.canevas.gettags("current")
        if "carre" in lestags:
            self.carrebouge=1
            
    def forgotclick(self,evt):
        self.carrebouge=0
        
    def miseajour(self,modele):
        self.canevas.delete(ALL)
        self.canevas.create_rectangle(50,50,400,400, fill="white")
        for i in modele.rectangles:
            self.canevas.create_rectangle(i.x1,i.y1,i.x2,i.y2,fill="blue", tags=("rectangle"))
        j=modele.carre
        self.canevas.create_rectangle(j.x1,j.y1,j.x2,j.y2,fill="yellow", tags=("carre"))

 


        

            

        
        
        
        
        
        
        
        
        
        
        
        