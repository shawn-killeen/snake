from modeles.case import Case
from enum import Enum


class CaseSerpent(Case) :
     
    allongerAuTick = False
     
    def __init__(self, grosseurGrille=0, x=0, y=0, parent=None, enfant=None ):
        super().__init__(grosseurGrille, x, y)
        self._parent = parent
        self._enfant = enfant
        
    def getParent(self):
        return self._parent
    
    def getEnfant(self):
        return self._enfant
    
    def setEnfant(self, enfant):
        self._enfant = enfant
        
    def getTete(self):
        parent = self

        while(True):
            nouveau = parent.getParent()
            if nouveau is not None:
                parent = nouveau
            else:
                break
        
        return parent
    
    def initierBouger(self, direction):
        tete = self.getTete()
        tete._bougerTete(direction)
    
    def _bougerTete(self, direction):
        nouveauX = self._x
        nouveauY = self._y
        
        if direction is "up":
            nouveauY = nouveauY - 1
        elif direction is "down":
            nouveauY = nouveauY + 1
        elif direction is "left":
            nouveauX = nouveauX - 1
        elif direction is "right":
            nouveauX = nouveauX + 1
        
        if nouveauX >= 0 and nouveauX < self._grosseurGrille:
            if nouveauY >= 0 and nouveauY < self._grosseurGrille:
                
                tempX = self._x
                tempY = self._y
                
                self._x = nouveauX
                self._y = nouveauY
                
                if(self._enfant is not None):
                    self._enfant._bouger(tempX, tempY)
                elif(CaseSerpent.allongerAuTick is True):
                    self._allonger(tempX, tempY, parent=self)
                
    
    def _bouger(self, x, y):
        
        tempX = self._x
        tempY = self._y
        
        self._x = x
        self._y = y
        
        if(self._enfant is not None):
            self._enfant._bouger(tempX, tempY)
        elif(CaseSerpent.allongerAuTick is True):
            self._allonger(tempX, tempY, parent=self)
    
    def _allonger(self, x, y, parent):
        nouveau = CaseSerpent(parent.getGrosseurGrille(), x, y, parent)
        parent.setEnfant(nouveau)
        CaseSerpent.allongerAuTick = False