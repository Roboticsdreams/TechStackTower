import unittest

from leetcode.problems import program3


class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.longsubstrobj = program3.LongestSubstring()

    def test_lengthOfLongestSubstring_Test01(self):
        result = self.longsubstrobj.lengthOfLongestSubstring("abcabcbb")
        expected = 3
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_Test02(self):
        result = self.longsubstrobj.lengthOfLongestSubstring("bbbbb")
        expected = 1
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_Test03(self):
        result = self.longsubstrobj.lengthOfLongestSubstring("pwwkew")
        expected = 3
        self.assertEqual(result, expected)

    def test_lengthOfLongestSubstring_Test04(self):
        result = self.longsubstrobj.lengthOfLongestSubstring("")
        expected = 0
        self.assertEqual(result, expected)

    def test_main(self):
        result = program3.longestsubstring_main()
        expected = 3
        self.assertEqual(result, expected)
