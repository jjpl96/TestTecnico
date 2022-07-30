import string 
import unittest

def find_missing_letter(chars):
    charset = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for letter in charset[charset.index(chars[0]):]:
        if letter not in chars:
            return letter[0]


class MyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')


# run the test
unittest.main()