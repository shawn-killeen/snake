# Shawn Killeen - Travail Pratique Synthese
# College Montmorency - H2021 4B5 - S. Deschenes

from datetime import datetime
import sqlite3

class Score ():
    
    FICHIER_DB = "./snake.db"
    TABLE_SCORE = "score"  
    
    ####################################
    ##            DUNDERS             ##
    ####################################
    
    def __init__(self, nom, score, date=None):
        self._nom = nom
        self._score = score
        
        if date is None: 
            self._date = datetime.now
        else: 
            self._date = date
            
    def __repr__(self):
        affichage = "%s %s %s" %  (str(self.getScore()), str(self.getNom()), str(self.getDate()))
        return affichage
    
    ####################################
    ##            GETTERS             ##
    ####################################
    
    def getNom(self): return self._nom
    
    def getScore(self): return self._score        
    
    def getDate(self): return self._date
    
    ####################################
    ##            DONNEES             ##
    ####################################
    
    # Methode de classe pour obtenir les scores de la base de donnee
    # En cas que la bd ne marche pas, le retour est une liste vide
    @classmethod
    def chargerScores(cls):
        scores = []
            
        try:
            # Preparation
            connexion = sqlite3.connect(cls.FICHIER_DB)
            curseur = connexion.cursor()
            
            # Requete
            requete = "SELECT nom, score, date FROM score"
            curseur.execute(requete)
            
            # Transformation
            for donnee in curseur.fetchall():
                score = Score(donnee[0], donnee[1], donnee[2])
                scores.append(score)
        
            curseur.close()
            
        except sqlite3.Error as error:
            print("Erreur de connection a la base de donnee", error)
        finally:
            if connexion: connexion.close()
        return scores
    
    
    # La sauvegrade dans la base de donnes d'un score
    def sauvegarder(self):
        try: 
            # Preparation
            connexion = sqlite3.connect(self.FICHIER_DB)
            curseur = connexion.cursor()
            
            # Requete
            requete = "INSERT INTO "+self.TABLE_SCORE+" (nom, score, date) VALUES (?, ?, ?)"
            curseur.execute(requete, (self.getNom(), self.getScore(), datetime.now()))     
            connexion.commit()
            
            curseur.close()
        except sqlite3.Error as error:
            print("Erreur de connection a la base de donnee", error)
        finally:
            if connexion: connexion.close()
    
    