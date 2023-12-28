# test_my_math.py
import unittest
from infix_parser import parse, to_infix_tokens

class TestMyMath(unittest.TestCase):

    def setUp(self):
        self.precedence_order = {
            "*": 2,
            "/": 2,
            "+": 1,
            "-": 1
        }

    def test_to_infix_tokens(self):
        self.assertEqual(to_infix_tokens("2+3*5", self.precedence_order), ["2", "+", "3", "*", "5"])
        self.assertEqual(to_infix_tokens("2.78  + 3 * 5.5", self.precedence_order), ["2.78", "+", "3", "*", "5.5"])


    def test_parse(self):
        self.assertEqual(parse("2 + 3 * 5", self.precedence_order), 17)
        self.assertEqual(parse("3 * 7 - 10", self.precedence_order), 11)
        self.assertEqual(parse("10 / 2.5 - 4", self.precedence_order), 0)

    def test_parse_parentheses(self):
        self.assertEqual(parse("( 2 + 3 ) * 5", self.precedence_order), 25)
        self.assertEqual(parse("3 * ( 7 - 10 )", self.precedence_order), -9)


if __name__ == '__main__':
    unittest.main()
