from modeles.case import Case
from enum import Enum
import math

class CaseSerpent(Case) :
    
    ####################################
    ##     VARIABLES DE CLASSE        ##
    ####################################
    
    _serpent = [] # les cases de serpents (pour la detection de collision)
    _allongerAuTick = 0 # Flag pour rajouter une case
     
    ####################################
    ##            DUNDERS             ##
    ####################################
     
    def __init__(self, grosseurGrille=0, x=0, y=0, parent=None, enfant=None ):
        super().__init__(grosseurGrille, x, y)
        self._parent = parent
        self._enfant = enfant
        
        CaseSerpent._serpent.append(self)
    
    ####################################
    ##            GETTERS             ##
    ####################################
    
    def getParent(self):
        return self._parent
    
    def getEnfant(self):
        return self._enfant
    
    # Parcours les parents pour trouver la tete
    def getTete(self):
        parent = self

        while(True):
            nouveau = parent.getParent()
            if nouveau is not None:
                parent = nouveau
            else:
                break
        
        return parent
    
    ####################################
    ##            SETTERS             ##
    ####################################
    
    def setEnfant(self, enfant):
        self._enfant = enfant
     
    ####################################
    ##            CLASSE              ##
    ####################################
    
    @classmethod
    def genererSerpent(cls, grosseurGrille):
        initiale = math.floor(grosseurGrille/2)
        return CaseSerpent(grosseurGrille, x=initiale, y=initiale, parent=None, enfant=None )
    
    @classmethod
    def effacerSerpent(cls):
        cls._serpent = []
    
    @classmethod
    def ajouterFileAllonger(cls, nbr=1):
        cls._allongerAuTick = cls._allongerAuTick + nbr
    
    @classmethod
    def diminuerFileAllonger(cls, nbr=1):
        valeur = cls._allongerAuTick - nbr if cls._allongerAuTick - nbr >= 0 else 0
        cls._allongerAuTick = valeur
        
    @classmethod
    def doitAllonger(cls):
        return True if cls._allongerAuTick > 0 else False
    
    @classmethod
    def checkCaseLibre(cls, x, y):
        libre = True
        for case in cls._serpent:
            if case.getX() == x:
                if case.getY() == y:
                    libre = False
                    break
        return libre
        
    ####################################
    ##           MOUVEMENT            ##
    ####################################
    
    # La seul methode qui doit etre appeller de l'exterieur
    # Elle declanche le reste des cases
    def initierBouger(self, direction):
        tete = self.getTete()
        mort = tete._bougerTete(direction)
        return mort
    
    # Commence l'iteration dans tout les cases de serpents
    def _bougerTete(self, direction):
        mort = False
        
        nouveauX = self._x
        nouveauY = self._y
        
        # La tete est la seule case qui a une nouvelle position
        # les autres prennent elle d'un autre case
        if direction == "up":
            nouveauY = nouveauY - 1
        elif direction == "down":
            nouveauY = nouveauY + 1
        elif direction == "left":
            nouveauX = nouveauX - 1
        elif direction == "right":
            nouveauX = nouveauX + 1
        
        # Verifie les collisions avant de bouger
        if (nouveauX >= 0 and nouveauX < self._grosseurGrille # Pour les murs
            and nouveauY >= 0 and nouveauY < self._grosseurGrille):  
                
                if(CaseSerpent.checkCaseLibre(nouveauX, nouveauY)): # Pour le serpent
                    
                    # Bouge
                    self._bouger(nouveauX, nouveauY)
                
        # Sinon meurt
                else: 
                    mort = True
        else: mort = True
        
        return mort
                    
                
    
    def _bouger(self, x, y):
        
        # Les valeurs a stocker temporairement pour donner a une autre partie du serpent
        tempX = self._x
        tempY = self._y
        
        # On bouge (l'emplacement est valide vu que cest la place d'un autre cellules qui a deja ete la tete,
        # donc a deja fait la verification)
        self._x = x
        self._y = y
        
        # Verifie si une case prend la place (enfant ou nouvelle case)
        if(self._enfant is not None):
            self._enfant._bouger(tempX, tempY)
        elif(CaseSerpent.doitAllonger()):
            self._allonger(tempX, tempY, parent=self)
            
    # On rajoute une cellule
    def _allonger(self, x, y, parent):
        nouveau = CaseSerpent(parent.getGrosseurGrille(), x, y, parent)
        parent.setEnfant(nouveau)
        CaseSerpent.diminuerFileAllonger()