from vues.partie import Partie
from vues.sauvegarde import Sauvegarde
from vues.input import Input
from vues.output import Output
from controleurs.logique import Logique
from modeles.config import Config
from modeles.score import Score
from tkinter import Tk
from threading import Thread
from time import sleep

class Controleur(Tk):
    
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self):
        super().__init__()

        self._inputNom = "Inconnu"

        self._config = Config.charger()

        self.title("Snake - Shawn Killeen")
        self._partie = Partie(self, self, config=self._config)
        
        self._input = Input(self._config)
        self._output = Output()

        self._logique = Logique(controleur=self, config=self._config , vue=self._partie, direction=self._input.getDirection, output=self._output)
    
        self.chargerHighscores()
    
        self._partie.mainloop()
        
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def chargerHighscores(self):
        scores = Score.chargerScores()
        self._partie.afficherHighscores(scores)
        
    def sauvegarderScore(self, valeur):
        
        if(valeur > 0):
            # Obtenir le nom du joueur
            popup = Tk()
            sauvegarde = Sauvegarde(popup, self, valeur)
            sauvegarde.mainloop()
            
            # Creer et sauvegarder le score
            score = Score(self._inputNom, valeur)
            score.sauvegarder()
            
            # Reload les scores
            self.chargerHighscores()
        
    
    ####################################
    ##            ACTIONS             ##
    ####################################
    # Callbacks des boutons de l'interface
    
    def actionDemarrer(self):
        self._logique.demarrer()
    
    def actionOptions(self):
        pass
    
    def actionQuitter(self):
       self._logique.arreterLoop()
       self._input.arreterLoop()
       self.quit()
       
    def actionRecevoirNom(self, valeur):
        self._inputNom = valeur