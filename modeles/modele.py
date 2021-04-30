from .score import Score
import sqlite3

class Modele:
    
    FICHIER_DB = "./snake.db"
    TABLE_DB = "score"
    FICHIER_CONFIG = "./config.json"
    
    
    def _alive(self):
        alive = self.connection is not None
        if not alive: print("Impossible de continuer (_alive), connection est null")
        return alive
    
    def _chargerDB(self):
        try:
            self.connection = sqlite3.connect(self.FICHIER_DB)
        except sqlite3.Error as error:
            print("Erreur d'ouverture de bd: " + str(error))
    
    def _fermerBD(self):
        if self._alive():
            try:
                self.connection.close()
            except sqlite3.Error as error:
                print("Erreur de fermeture de bd: " + str(error))
           
    def _tableExiste(self):
        existe = False
        
        self._chargerDB()
        
        if self._alive():
            try:
                curseur = self.connection.cursor()
                curseur.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"+self.TABLE_DB+"'")
                if(curseur.fetchone()[0]==1): existe = True
            except sqlite3.Error as error:
                print("Erreur de sql (_tableExiste): " + str(error))
               
        if not existe: print("Impossible de continuer (_tableExiste), table est null") 
        return existe
    
    def _chargerScores(self, limit=5):
        scores = []
        
        self._chargerDB()
        
        if self._alive() and self._tableExiste():
            
            try:
                curseur = self.connection.cursor()
                curseur.execute("SELECT nom, score, date FROM " + self.TABLE_DB)
                    
                scoresSQL = curseur.fetchall()
                
                for score in scoresSQL:
                    scores.append(Score(score[0], score[1], score[2]))
                    
            except sqlite3.Error as error:
                print("Erreur de chargement des scores: " + str(error))
        
            self._fermerBD()
            
        return scores
            
    
    def _sauvegarderScore(self, score):
        pass
    
    def _chargerConfig(self):
        pass
    
    def _sauvegarderConfig(self, config):
        pass