from modeles.case import Case
import unittest

class TestModeleSerpent(unittest.TestCase):

    def test_x(self):
        objet = Case(x=30)
        self.assertEqual(objet.getX(), 30)
        objet.setX(50)
        self.assertEqual(objet.getX(), 50)
    
    def test_y(self):
        objet = Case(y=30)
        self.assertEqual(objet.getY(), 30)
        objet.setY(50)
        self.assertEqual(objet.getY(), 50)
             
    def test_grille(self):
        objet = Case(grosseurGrille=30)
        self.assertEqual(objet.getGrosseurGrille(), 30)