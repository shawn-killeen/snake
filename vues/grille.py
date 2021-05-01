from modeles.config import Config
from tkinter import Canvas
from time import sleep

class Grille(Canvas):
    
    ####################################
    ##          CONSTANTES            ##
    ####################################
    
    TAILLE = 400
    COULEURS_FOND = ("green", "lightgreen")
    COULEURS_SERPENT = "purple"
    COULEUR_POMME = "red"
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)
        self.config = Config.charger()
    
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
        largeurGrille = self.config.getGrosseurGrille() # Nombre de cases par row/col
        casePixel = self.TAILLE/largeurGrille # Grosseur tkinter

        # On dessine
        for y in range(largeurGrille):
            for x in range(largeurGrille):
                coord = (x*casePixel, y*casePixel, x*casePixel + casePixel, y*casePixel + casePixel)
                self.create_rectangle(coord, fill=Jeu._trouverCouleur(x,y), outline='')