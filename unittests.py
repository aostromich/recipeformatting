import unittest

from main import universal_replace

class TestUniversalReplace(unittest.TestCase):
    def test_singular_tbs(self):
        self.assertEqual(universal_replace("1 tbsp"), "1 tablespoon")
        self.assertEqual(universal_replace("1 tbsp."), "1 tablespoon")
        self.assertEqual(universal_replace("1 tbs"), "1 tablespoon")
        self.assertEqual(universal_replace("1 tbs."), "1 tablespoon")
        self.assertEqual(universal_replace("1 TBS"), "1 tablespoon")
        self.assertEqual(universal_replace("1/2 tbsp."), "1/2 tablespoon")
        self.assertEqual(universal_replace("¾ tbsp."), "¾ tablespoon")
    
    def test_singular_tsp(self):
        self.assertEqual(universal_replace("1 tsp"), "1 teaspoon")
        self.assertEqual(universal_replace("1 tsp."), "1 teaspoon")
        self.assertEqual(universal_replace("1 TSP"), "1 teaspoon")
        self.assertEqual(universal_replace("1/2 TSP"), "1/2 teaspoon")
        self.assertEqual(universal_replace("½ TSP"), "½ teaspoon")
    
    def test_plural_tbsp(self):
        self.assertEqual(universal_replace("1 1/2 tbsp"), "1 1/2 tablespoons")
        self.assertEqual(universal_replace("12 3/4 tbsp"), "12 3/4 tablespoons")
        self.assertEqual(universal_replace("10 tbsp"), "10 tablespoons")
        self.assertEqual(universal_replace("4 ½ tbsp."), "4 ½ tablespoons")
        self.assertEqual(universal_replace("11 ¾ tbsp."), "11 ¾ tablespoons")
    
    def test_plural_tsp(self):
        self.assertEqual(universal_replace("2 1/3 tsp"), "2 1/3 teaspoons")
        self.assertEqual(universal_replace("20 1/2 tsp."), "20 1/2 teaspoons")
        self.assertEqual(universal_replace("12 tsp."), "12 teaspoons")
        self.assertEqual(universal_replace("14 ½ tsp."), "14 ½ teaspoons")
    
    def test_ingredient_renames(self):
        self.assertEqual(universal_replace("1 bunch scallions"), "1 bunch green onions")
        self.assertEqual(universal_replace("Scallions, chopped finely"), "Green onions, chopped finely")

if __name__ == "__main__":
    unittest.main()