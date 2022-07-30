import unittest
import functions



class MyTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(functions.validate_pin("1"), False, "Wrong output for '1'")
        self.assertEqual(functions.validate_pin("12"), False, "Wrong output for '12'")
        self.assertEqual(functions.validate_pin("123"), False, "Wrong output for'123'")
        self.assertEqual(functions.validate_pin("12345"), False, "Wrong output for'12345'")
        self.assertEqual(functions.validate_pin("1234567"), False, "Wrong output for'1234567'")
        self.assertEqual(functions.validate_pin("-1234"), False, "Wrong output for '-1234'")
        self.assertEqual(functions.validate_pin("-12345"), False, "Wrong output for '-12345'")
        self.assertEqual(functions.validate_pin("1.234"), False, "Wrong output for'1.234'")
        self.assertEqual(functions.validate_pin("00000000"), False, "Wrong output for'00000000'")


    def test_another_character(self):
        self.assertEqual(functions.validate_pin("a234"), False, "Wrong output for'a234'")
        self.assertEqual(functions.validate_pin(".234"), False, "Wrong output for'.234'")

    def test_should_return_true(self):
        self.assertEqual(functions.validate_pin("1234"),True, "Wrong output for'1234'")
        self.assertEqual(functions.validate_pin("0000"),True, "Wrong output for'0000'")
        self.assertEqual(functions.validate_pin("1111"),True, "Wrong output for'1111'")
        self.assertEqual(functions.validate_pin("123456"),True, "Wrong output for'123456'")
        self.assertEqual(functions.validate_pin("098765"),True, "Wrong output for'098765'")
        self.assertEqual(functions.validate_pin("000000"),True, "Wrong output for'000000'")
        self.assertEqual(functions.validate_pin("123456"),True, "Wrong output for'123456'")
        self.assertEqual(functions.validate_pin("090909"),True, "Wrong output for'090909'")
# run the test
unittest.main()

