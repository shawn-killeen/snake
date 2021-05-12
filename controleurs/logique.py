from vues.partie import Partie
from modeles.config import Config
from modeles.caseSerpent import CaseSerpent
from modeles.casePomme import CasePomme
from threading import Thread
from time import sleep
import math

class Logique:
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, controleur, config, vue, direction):
        self._controlleur = controleur
        self._config = config
        self._vue = vue
        self._direction = direction
        
        # init de variables pour qu'elle existe en tout temps
        self.estDemarrer = False # une partie dans le thread
        self.score = 0
        
        # Boucle
        self.demarrerLoop()
    
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def demarrerLoop(self):
        # boucle
        
        self.stopBoucle = False
        thread = Thread(target = self._gameLoop)
        thread.start()
        
    def arreterLoop(self):
        self.stopBoucle = True
        
    ####################################
    ##             SNAKE              ##
    ####################################    

    def ajouterAuScore(self, nbr=1):
        self.score = self.score + nbr
        
    def resetScore(self):
        self.score = 0
        
    def getScore(self):
        return self.score

    def demarrer(self):
        
        # Init du jeu
        self.estDemarrer = True
        self.resetScore()
        self._vue.afficherScore(self.getScore())
        self._tick = 1/self._config.getTickRate()
        self._grille = self._vue.getGrille()
        
        # Reset de la partie precedente (on verifie pas, pas besoin de performance ici :') )
        self._grille.generer()
        CaseSerpent.effacerSerpent()
        
        # Nouveau snake!
        self._serpent = CaseSerpent.genererSerpent(self._config.getGrosseurGrille())
        self._pomme = CasePomme.genererPomme(self._config.getGrosseurGrille())
        CaseSerpent.ajouterFileAllonger(2)

    def _gameLoop(self):
        
        mort = False # Sauvegarde la mort en dehors de la loop
        
        while(not self.stopBoucle):
            
            if(self.estDemarrer):
                if not mort:
                    # On modifie les objets du jeu
                    mort = self._serpent.initierBouger(self._direction())
                    
                    if(self._pomme.toucheSerpent()):
                        self._pomme = CasePomme.genererPomme(self._config.getGrosseurGrille())
                        CaseSerpent.ajouterFileAllonger(1)
                        self.ajouterAuScore()
                        self._vue.afficherScore(self.getScore())     
                    
                    # On affiche le jeu
                    self._grille.dessinerSerpent(self._serpent)
                    self._grille.dessinerPomme(self._pomme)
                    
                    # Deroulement du jeu
                    sleep(self._tick)
                        
                else:
                    # Affiche la carcasse du pauvre serpent et met le jeu sur pause
                    self._grille.dessinerSerpent(self._serpent, mort=True)
                    self.estDemarrer = False
                    mort = False
                    self._controlleur.sauvegarderScore(self.getScore())
            else:
                sleep(1) # Patiente pour une nouvelle partie (Un seul thread pour tout les parties)
    
    