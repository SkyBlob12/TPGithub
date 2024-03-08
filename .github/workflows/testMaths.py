class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        # Test case 1
        result1 = SimpleMath.addition(2, 3)
        self.assertEqual(result1, 5)

        # Test case 2
        result2 = SimpleMath.addition(-1, 5)
        self.assertEqual(result2, 4)

        # Test case 3
        result3 = SimpleMath.addition(0, 0)
        self.assertEqual(result3, 0)

    def test_soustraction(self):
        # Test case 1
        result1 = SimpleMath.soustraction(5, 2)
        self.assertEqual(result1, 3, "La soustraction de 5 et 2 devrait être égale à 3")

        # Test case 2
        result2 = SimpleMath.soustraction(-1, 5)
        self.assertEqual(result2, -6, "La soustraction de -1 et 5 devrait être égale à -6")

        # Test case 3
        result3 = SimpleMath.soustraction(0, 0)
        self.assertEqual(result3, 0, "La soustraction de 0 et 0 devrait être égale à 0")