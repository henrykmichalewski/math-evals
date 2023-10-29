import unittest
from sympy import Interval
from fractions import Fraction

import minerva_python_prompt


class TestMinervaExercises(unittest.TestCase):

    def setUp(self):
        """
        Setup function to execute function definitions before each test.
        """
        global_vars = globals()
        exec(minerva_python_prompt.MINERVA_PYTHON_PROMPT, global_vars)

    def test_exercise1(self):
        """
        Test function for exercise1.
        """
        result = exercise1()
        # Expected result is the interval [2, 5)
        self.assertEqual(result, Interval.Ropen(2, 5))

    def test_exercise2(self):
        """
        Test function for exercise2.
        """
        result = exercise2()
        # Expected result is 24
        self.assertEqual(result, 24)

    def test_exercise3(self):
        """
        Test function for exercise3.
        """
        result = exercise3()
        # Expected result is 16
        self.assertEqual(result, 16)

    def test_exercise4(self):
        """
        Test function for exercise4.
        """
        result = exercise4()
        # Expected result is -2/3
        self.assertEqual(result, -Fraction(2, 3))

if __name__ == "__main__":
    unittest.main()
