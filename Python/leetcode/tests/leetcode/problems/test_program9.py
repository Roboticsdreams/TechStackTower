import unittest

from leetcode.problems import program9


class TestPalindromeNumber(unittest.TestCase):
    def setUp(self):
        self.palindromenumberobj = program9.PalindromeNumber()

    def test_isPalindrome_Test01(self):
        result = self.palindromenumberobj.isPalindrome(121)
        expected = True
        self.assertEqual(result, expected)

    def test_isPalindrome_Test02(self):
        result = self.palindromenumberobj.isPalindrome(1212)
        expected = False
        self.assertEqual(result, expected)

    def test_main(self):
        result = program9.palindromenumber_main()
        expected = True
        self.assertEqual(result, expected)