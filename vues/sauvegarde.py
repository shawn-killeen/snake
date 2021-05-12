
from tkinter import *

class Sauvegarde(Frame):
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, master, controleur, score):
        super().__init__(master)
        self._master = master
        self._controleur = controleur
        self._score = score
        
        self._preparerInterface()
        
    ####################################
    ##           INTERFACE            ##
    ####################################
    
    def _preparerInterface(self):
        
        # Definitions
        self._boutonSauvegarde = Button(self, text="Sauvegarder", width=32, height=2, command=self.sauvegarder)
        self._labelScore = Label(self, text="Score: "+str(self._score) )
        self._labelNom = Label (self, text="Entrez votre nom: ")
        self._entryNom = Entry(self, width=32)
        
        # Layout
        self._labelScore.grid(row=0, padx=5)
        self._labelNom.grid(row=1,padx=5)
        self._entryNom.grid(row=2, padx=5)
        self._boutonSauvegarde.grid(row=3, padx=5)

        # Applique le layout
        self.pack()
        
    def sauvegarder(self):
        self._controleur.actionRecevoirNom(self._entryNom.get())
        self._master.destroy()