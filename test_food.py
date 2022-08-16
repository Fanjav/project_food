"""Module Test unitaire pour la classe Food
Les propriétés:
   . name
   . calories
   . fat (lipides)
   . carbss (glucides)
   . protein (protéines)
les valeurs associées à ces propriétés se feront sur une base de 100 grammes
**Projet réalisé par Phuc PHAM NGOC et Fanjavola RAHANTAHARIMANANA
"""
import unittest
from food import Food

class TestFood(unittest.TestCase):
    """Test module class for Food class"""
    def setUp(self) -> None:
        """Setup some objects from Food class for tests"""
        print('Setup objects Food')
        self.food1 = Food('tomate')
        self.food2 = Food('melon')
        self.food3 = Food('mayonnaise')

    def test_check_fat(self) -> bool:
        """Tests for check_fat method of Food class"""
        print('Test check_fat')
        self.assertEqual(self.food1.check_fat(),False)
        self.assertEqual(self.food2.check_fat(),False)
        self.assertEqual(self.food3.check_fat(),True)
