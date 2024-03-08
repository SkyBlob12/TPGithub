import unittest

class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b

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

if __name__ == '__main__':
    unittest.main()