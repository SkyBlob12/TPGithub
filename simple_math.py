"""
    This module is used to answer questions of the CI/CD assignment.
"""

import unittest

class SimpleMath:
    """
        This class does simple math.
    """
    @staticmethod
    def addition(a, b):
        """
            This method takes two numbers and return their sum.
        """
        return a + b

    @staticmethod
    def soustraction(a, b):
        """
            This method takes two numbers and return their difference.
        """
        return a - b

class TestSimpleMath(unittest.TestCase):
    """
        This class tests the method of the SimpleMath class.
    """
    def test_addition(self):
        """
            This method tests exclusively the SimpleMath class 'addition' method.
        """
        self.assertEqual(SimpleMath.addition(2, 3) , 5)

    def test_soustraction(self):
        """
            This method tests exclusively the SimpleMath class 'soustraction' method
        """
        self.assertEqual(SimpleMath.soustraction(7, 4), (3))

if __name__== "__main__":
    unittest.main()