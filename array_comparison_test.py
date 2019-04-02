import unittest
from array_comparison import comp


class TestArrayComparison(unittest.TestCase):

    def test__with_valid_input(self):
        a = [2, 5, 8]
        b = [25, 64, 4]
        self.assertTrue(comp(a, b))

    def test_with_longer_valid_input(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertTrue(comp(a, b))

    def test_with_invalid_input(self):
        a = [121, 144, 19, 161, 19, 144, 19, 11]
        b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertFalse(comp(a, b))

    def test_with_none_input(self):
        a = None
        b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
        self.assertFalse(comp(a, b))


if __name__ == "__main__":
    unittest.main()
