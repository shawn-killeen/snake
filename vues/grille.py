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
    COULEUR_SERPENT = "DarkOrchid2"
    COULEUR_MORT = "cyan4"
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
    
    # Refait tout les secteurs de la grille
    def generer(self):
        # On dessine
        for y in range(self.largeurGrille):
            for x in range(self.largeurGrille):
                self.dessinerCase(Case(x=x, y=y), couleur=Grille._trouverCouleur(x,y))
    
    # Parcours le serpent et dessine les cases
    def dessinerSerpent(self, serpent, mort=False):
        case = serpent.getTete()
        
        # Prend l'ancienne queue pour l'effacer
        # Vue qu'on a bouger, la derniere case n'est pu la
        efface = self.casePourEffacer
        if efface is not None:
            self.dessinerCase(efface, couleur=Grille._trouverCouleur(efface.getX(),efface.getY()))
        
        while True:
            
            # Changement de couleur si mort/vivant
            couleur = Grille.COULEUR_MORT if mort else Grille.COULEUR_SERPENT
            
            # Dessine
            self.dessinerCase(case, couleur)
            
            # Prend la prochaine case si elle existe
            if case.getEnfant() is not None:
                case = case.getEnfant()
            # Sinon on stock la queue
            else:
                self.casePourEffacer = Case(0, x=case.getX(), y=case.getY())
                break
    
    def dessinerPomme(self, case):
        self.dessinerCase(case, Grille.COULEUR_POMME)
    
    # Dessine une seul case
    def dessinerCase(self, case, couleur='black'):
        casePixel = self.casePixel # Pour raccourcir
        
        # Mechante belle ligne, c'est les 4 coins d'une case donc x1, y1, x2, y2
        coord = (case.getX()*casePixel, 
                 case.getY()*casePixel, 
                 case.getX()*casePixel + casePixel, 
                 case.getY()*casePixel + casePixel)
        
        # On dessine
        self.create_rectangle(coord, fill=couleur, outline='')