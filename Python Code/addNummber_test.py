import unittest
from addNumber import add

class addNumbersTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,2"), 3)
        
    def test_newline_delimiter(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_custom_delimiter_and_newline(self):
        self.assertEqual(add("//;\n1;2;3\n4"), 10)
        
    def test_negative_number(self):
        with self.assertRaises(Exception) as context:
            add("-1")
        self.assertEqual(str(context.exception), "Negatives not allowed: -1")

    def test_negative_numbers(self):
        with self.assertRaises(Exception) as context:
            add("-1,-2")
        self.assertEqual(str(context.exception), "Negatives not allowed: -1, -2")

    
        
if __name__ == '__main__':
    unittest.main()