import functools
import unittest

def persistence(n):
    t = 0

    while n > 9:
        n = functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        t += 1

    return t


class MyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(persistence(39), 3)
        self.assertEqual(persistence(4), 0)
        self.assertEqual(persistence(25), 2)
        self.assertEqual(persistence(999), 4)


# run the test
unittest.main()