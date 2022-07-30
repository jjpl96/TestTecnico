import unittest

def array_diff(a, b):
    if a == []: return a
    if b == []: return a
    for occurrence in b:
        if occurrence in a:
            a = list(filter(lambda val: val != occurrence, a))
    return a


class MyTest(unittest.TestCase):
    def test_fixed(self):
        self.assertEqual(array_diff([1,2], [1]), [2], "a was [1,2], b was[1], expected [2]")
        self.assertEqual(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEqual(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEqual(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEqual(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

# run the test
unittest.main()