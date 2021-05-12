from .grille import Grille
from tkinter import *

class Partie(Frame):
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, controleur, master, config):
        super().__init__(master)
        self._controleur = controleur
        self._master = master
        self._config = config
        
        self._preparerInterface()
        
    ####################################
    ##           INTERFACE            ##
    ####################################
    
    def _preparerInterface(self):
        
        # Definitions
        self._boutonDemarrer = Button(self, text="Démarrer", width=32, height=2, command=self._controleur.actionDemarrer)
        self._boutonOptions = Button(self, text="Options", width=32, height=2, command=self._controleur.actionOptions)
        self._boutonQuitter = Button(self, text="Quitter", width=32, height=2, command=self._controleur.actionQuitter)
        self._labelScoreEtiquette = Label(self, text="Score: " )
        self._labelScoreValeur = Label(self, text="0")
        self._grille = Grille(self,width=400, height=400,bg="green", config=self._config)
        self._highscores = Listbox(self, width=32, height=10)
        
        # Layout
        self._boutonDemarrer.grid(row=0, column=1, columnspan=2, padx=5)
        self._boutonOptions.grid(row=1, column=1, columnspan=2,padx=5)
        self._boutonQuitter.grid(row=2, column=1, columnspan=2, padx=5)
        self._labelScoreEtiquette.grid(row=3, column=1)
        self._labelScoreValeur.grid(row=3, column=2)
        self._highscores.grid(row=5, column=1, columnspan=2)
        self._grille.grid(row=0, column=0, rowspan=6)

        # Applique le layout
        self.pack()
        
        # Genere la partie
        self._grille.generer()
        
    def getGrille(self):
        return self._grille
    
    def afficherScore(self, score):
        self._labelScoreValeur.config(text=score)
        
    def afficherHighscores(self, scores):
        self._highscores.delete(0, self._highscores.size()-1)
        
        for score in scores:
            self._highscores.insert (END, score)