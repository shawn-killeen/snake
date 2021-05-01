from .grille import Grille
from tkinter import *

class Partie(Frame):
    
    def __init__(self, controleur, master):
        super().__init__(master)
        self._controleur = controleur
        self._master = master
        
        self._preparerInterface()
    
    def _preparerInterface(self):
        
        self._boutonDemarrer = Button(self, text="Démarrer", command=self._controleur.actionDemarrer)
        self._boutonOptions = Button(self, text="Options", command=self._controleur.actionOptions)
        self._boutonQuitter = Button(self, text="Quitter", command=self._controleur.actionQuitter)
        self._labelScoreEtiquette = Label(self, text="Score: ")
        self._labelScoreValeur = Label(self, text="0")
        self._grille = Grille(self)
        
        self._boutonDemarrer.grid(row=0, column=0)
        self._boutonOptions.grid(row=0, column=1)
        self._boutonQuitter.grid(row=0, column=2)
        self._labelScoreEtiquette.grid(row=1, column=0)
        self._labelScoreValeur.grid(row=1, column=1)
        self._grille.grid(row=2, column=0, columnspan=3)
        
        self.pack()
    
    def afficherGrille(self, grille):
        pass
    