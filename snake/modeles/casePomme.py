from modeles.case import Case
from modeles.caseSerpent import CaseSerpent
from enum import Enum
import random


class CasePomme(Case) :
    
    ####################################
    ##     VARIABLES DE CLASSE        ##
    ####################################
     
    ####################################
    ##            DUNDERS             ##
    ####################################
     
    def __init__(self, grosseurGrille=0, x=0, y=0):
        super().__init__(grosseurGrille, x, y)
    
    ####################################
    ##            GETTERS             ##
    ####################################
    
    ####################################
    ##            SETTERS             ##
    ####################################
     
    ####################################
    ##            CLASSE              ##
    ####################################
    
    @classmethod
    def genererPomme(cls, grosseurGrille):
        position = cls.trouverPositionLibre(grosseurGrille)
        return CasePomme(grosseurGrille, position.getX(), position.getY())
        
    @classmethod
    def trouverPositionLibre(cls, grosseurGrille):
        x = 0
        y = 0
        
        while True:
         x = random.randrange(0, grosseurGrille-1)
         y = random.randrange(0, grosseurGrille-1)
         
         if(CaseSerpent.checkCaseLibre(x, y)):
             break
         
        return Case(x=x, y=y)
         
         
    
    ####################################
    ##             POMME              ##
    ####################################
    
    def toucheSerpent(self):
        if not CaseSerpent.checkCaseLibre(self.getX(), self.getY()):
            return True
        else:
            return False