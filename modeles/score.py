
from datetime import datetime
import sqlite3

class Score ():
    
    FICHIER_DB = "./snake.db"
    TABLE_SCORE = "score"  
    
    def __init__(self, nom, score, date=None):
        self._nom = nom
        self._score = score
        
        if date is None: 
            self._date = datetime.now
        else: 
            self._date = date
            
    def getNom(self): return self._nom
    
    def getScore(self): return self._score        
    
    def getDate(self): return self._date
    
    def __repr__(self):
        affichage = "%s %s %s" %  (str(self.getScore()), str(self.getNom()), str(self.getDate()))
        return affichage
    
    @classmethod
    def chargerScores(cls):
        scores = []
            
        try:
            connexion = sqlite3.connect(cls.FICHIER_DB)
            
            curseur = connexion.cursor()
            
            requete = "SELECT nom, score, date FROM score"
            
            curseur.execute(requete)
            
            for donnee in curseur.fetchall():
                score = Score(donnee[0], donnee[1], donnee[2])
                scores.append(score)
            
            curseur.close()
        except sqlite3.Error as error:
            print("Erreur de connection a la base de donnee", error)
        finally:
            if connexion: connexion.close()
        return scores
    
    
    
    def sauvegarder(self):
        try:
            connexion = sqlite3.connect(self.FICHIER_DB)
            
            curseur = connexion.cursor()
            
            
            requete = "INSERT INTO "+self.TABLE_SCORE+" (nom, score, date) VALUES (?, ?, ?)"
            params = (self.getNom(), self.getScore(), datetime.now())
            
            curseur.execute(requete, params)
            
            connexion.commit()
            curseur.close()
        except sqlite3.Error as error:
            print("Erreur de connection a la base de donnee", error)
        finally:
            if connexion: connexion.close()
    
    