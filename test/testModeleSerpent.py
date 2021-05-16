from modeles.caseSerpent import CaseSerpent
import unittest

class TestModeleCase(unittest.TestCase):

    def test_longueur(self):
        CaseSerpent.effacerSerpent()
        objet1 = CaseSerpent()
        objet2 = CaseSerpent()
        self.assertEqual(len(CaseSerpent._serpent), 2)
             
    def test_caseLibre(self):
        objet = CaseSerpent(grosseurGrille=10, x=0, y=0)
        self.assertEqual(CaseSerpent.checkCaseLibre(x=0, y=0), False)
        self.assertEqual(CaseSerpent.checkCaseLibre(x=1, y=1), True)