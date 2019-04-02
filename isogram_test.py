import unittest
from isogram import is_isogram


class TestIsogram(unittest.TestCase):
    def test_isogram_returns_true(self):
        test_input = 'isogram'
        self.assertTrue(is_isogram(test_input))

    def test_empty_string_returns_true(self):
        test_input = ''
        self.assertTrue(is_isogram(test_input))

    def test_ignores_case_repeat_returns_false(self):
        test_input = 'moOse'
        self.assertFalse(is_isogram(test_input))

    def test_repeat_returns_false(self):
        test_input = 'aba'
        self.assertFalse(is_isogram(test_input))


if __name__ == '__main__':
    unittest.main()
