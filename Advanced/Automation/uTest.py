# importing unittest module
import unittest


class TestingStringMethods(unittest.TestCase):
    # string equal
    def test_string_equality(self):
        # if both arguments are then it's succes
        self.assertEqual('ttp' * 5, 'ttpttpttpttpttp')

    # comparing the two strings
    def test_string_case(self):
        # if both arguments are then it's succes
        self.assertEqual('Tutorialspoint'.upper(), 'TUTORIALSPOINT')

    # checking whether a string is upper or not
    def test_is_string_upper(self):
        # used to check whether the statement is True or False
        self.assertTrue('TUTORIALSPOINT'.isupper())
        self.assertFalse('TUTORIALSpoint'.isupper())

    def test_string_startswith(self):
        # Used the startswith() to identify the start of the string
        self.assertTrue('tutorialspoint'.startswith('putor'))
        self.assertFalse('tutorialspoint'.startswith('point'))


# running the tests
unittest.main(verbosity=2)