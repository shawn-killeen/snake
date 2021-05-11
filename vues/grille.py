from tkinter import Canvas
from time import sleep
from modeles.caseSerpent import CaseSerpent
from modeles.case import Case

class Grille(Canvas):
    
    ####################################
    ##          CONSTANTES            ##
    ####################################
    
    TAILLE = 400
    COULEURS_FOND = ("green", "lightgreen")
    COULEUR_SERPENT = "purple"
    COULEUR_POMME = "red"
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, master, config, **kwargs):
        super().__init__(master, kwargs)
        self._config = config
        
        self.largeurGrille = self._config.getGrosseurGrille() # Nombre de cases par row/col
        self.casePixel = self.TAILLE/self.largeurGrille # Grosseur tkinter
        self.casePourEffacer = None
    
    ####################################
    ##            HELPERS             ##
    ####################################

    # Si les deux coordonnes ne sont pas les deux paires ou impaires,
    # on retourne une couleur si elles le sont, on retourne l'autre couleur
    @classmethod
    def _trouverCouleur(cls, x, y):
        if (x%2 == 0 and y%2 == 1) or (x%2 == 1 and y%2 == 0): 
            return cls.COULEURS_FOND[0]
        else: 
            return cls.COULEURS_FOND[1]
    
    ####################################
    ##            GRILLE              ##
    ####################################
    
    def generer(self):
        # On dessine
        for y in range(self.largeurGrille):
            for x in range(self.largeurGrille):
                self.dessinerCase(Case(x=x, y=y), couleur=Grille._trouverCouleur(x,y))
    
    def dessinerSerpent(self, serpent):
        case = serpent.getTete()
        
        efface = self.casePourEffacer
        if efface is not None:
            self.dessinerCase(efface, couleur=Grille._trouverCouleur(efface.getX(),efface.getY()))
        
        while True:
            
            self.dessinerCase(case, Grille.COULEUR_SERPENT)
            
            if case.getEnfant() is not None:
                case = case.getEnfant()
            else:
                self.casePourEffacer = Case(0, x=case.getX(), y=case.getY())
                break
              
    def dessinerCase(self, case, couleur='black'):
        casePixel = self.casePixel
        coord = (case.getX()*casePixel, case.getY()*casePixel, case.getX()*casePixel + casePixel, case.getY()*casePixel + casePixel)
        self.create_rectangle(coord, fill=couleur, outline='')