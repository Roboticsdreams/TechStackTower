import unittest

from leetcode.problems import program5


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.longestpalindromeobj = program5.LongestPalindromic()

    def test_longestPalindrome_Test01(self):
        result = self.longestpalindromeobj.longestPalindrome("babad")
        expected = "bab"
        self.assertEqual(result, expected)

    def test_longestPalindrome_Test02(self):
        result = self.longestpalindromeobj.longestPalindrome("cbbd")
        expected = "bb"
        self.assertEqual(result, expected)

    def test_longestPalindrome_Test03(self):
        result = self.longestpalindromeobj.longestPalindrome("a")
        expected = "a"
        self.assertEqual(result, expected)

    def test_longestPalindrome_Test04(self):
        result = self.longestpalindromeobj.longestPalindrome("ac")
        expected = "a"
        self.assertEqual(result, expected)

    def test_longestPalindrome_Test05(self):
        result = self.longestpalindromeobj.longestPalindrome("caddymadam")
        expected = "madam"
        self.assertEqual(result, expected)

    def test_main(self):
        result = program5.longestpalindrome_main()
        expected = "bab"
        self.assertEqual(result, expected)
