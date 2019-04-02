import unittest
from remove_spaces import no_space


class TestRemoveSpaces(unittest.TestCase):
    def test_1(self):
        expected = 'nospaces'
        test_input = 'n o   sp  a c   e s'
        self.assertEqual(no_space(test_input), expected)

    def test_2(self):
        expected = 'thishasnospaceseither'
        test_input = 't h is ha s no spa  ce s e  i th  er      '
        self.assertEqual(no_space(test_input), expected)


if __name__ == '__main__':
    unittest.main()
