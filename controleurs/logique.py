from vues.partie import Partie
from modeles.config import Config
from modeles.caseSerpent import CaseSerpent
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
        
        # Boucle
        self.demarrerLoop()
    
    ####################################
    ##          CONTROLEUR            ##
    ####################################
    
    def demarrer(self):
        
        # Init du jeu
        self.estDemarrer = True
        self._tick = 1/self._config.getTickRate()
        self._grille = self._vue.getGrille()
        
        # Reset de la partie precedente (on verifie pas, pas besoin de performance ici :') )
        self._grille.generer()
        CaseSerpent.serpent = []
        
        # Nouveau snake!
        self._creerSerpent()
        CaseSerpent.ajouterFileAllonger(2)
    
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

    def _gameLoop(self):
        
        mort = False # Sauvegarde la mort en dehors de la loop
        
        while(not self.stopBoucle):
            
            if(self.estDemarrer):
                if not mort:
                    # On modifie les objets du jeu
                    mort = self._serpent.initierBouger(self._direction())
                    
                    # On affiche le jeu
                    self._grille.dessinerSerpent(self._serpent)
                    
                    # Deroulement du jeu
                    sleep(self._tick)
                        
                else:
                    # Affiche la carcasse du pauvre serpent et met le jeu sur pause
                    self._grille.dessinerSerpent(self._serpent, mort=True)
                    self.estDemarrer = False
                    mort = False
            else:
                sleep(1) # Patiente pour une nouvelle partie (Un seul thread pour tout les parties)
            
    # Creer une case de serpent et on le met au centre   
    def _creerSerpent(self):
        initiale = math.floor(self._config.getGrosseurGrille()/2)
        self._serpent =  CaseSerpent(self._config.getGrosseurGrille(), x=initiale, y=initiale, parent=None, enfant=None )
    
    