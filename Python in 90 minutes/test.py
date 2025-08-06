import unittest
from Python_in_90_minutes import cuber, solve_triangle  # replace with your actual file name (without .py)

class TestBasics(unittest.TestCase):
    def test_cuber(self):
        self.assertEqual(cuber(3), 27)
        self.assertEqual(cuber(), 8)  # default param test

    def test_solve_triangle(self):
        area, perimeter = solve_triangle(3, 4, 3, 4, 5)
        self.assertAlmostEqual(area, 6.0)
        self.assertEqual(perimeter, 12)

if __name__ == '__main__':
    unittest.main()