from enum import Enum

class Case:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, grosseurGrille=0, x=0, y=0):
        self._grosseurGrille = grosseurGrille
        self._x = x
        self._y = y
    
    ####################################
    ##            GETTERS             ##
    ####################################
    
    def getGrosseurGrille(self):
        return self._grosseurGrille
    
    def getX(self):
        return self._x
    
    def getY(self):
        return self._y
    
    ####################################
    ##            SETTERS             ##
    ####################################
    
    def setX(self, valeur):
        self._x = valeur
        
    def setY(self, valeur):
        self._y = valeur