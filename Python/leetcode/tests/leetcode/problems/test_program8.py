import unittest

from leetcode.problems import program8


class TestStringtoInteger(unittest.TestCase):
    def setUp(self):
        self.stringtointegerobj = program8.StringtoInteger()

    def test_myAtoi_Test01(self):
        result = self.stringtointegerobj.myAtoi("42")
        expected = 42
        self.assertEqual(result, expected)

    def test_myAtoi_Test02(self):
        result = self.stringtointegerobj.myAtoi("  -42")
        expected = -42
        self.assertEqual(result, expected)

    def test_myAtoi_Test03(self):
        result = self.stringtointegerobj.myAtoi("4193 with words")
        expected = 4193
        self.assertEqual(result, expected)

    def test_myAtoi_Test04(self):
        result = self.stringtointegerobj.myAtoi("words and 987")
        expected = 0
        self.assertEqual(result, expected)

    def test_myAtoi_Test05(self):
        result = self.stringtointegerobj.myAtoi("-91283472332")
        expected = -2147483648
        self.assertEqual(result, expected)

    def test_myAtoi_Test06(self):
        result = self.stringtointegerobj.myAtoi("000-321a")
        expected = 0
        self.assertEqual(result, expected)

    def test_myAtoi_Test07(self):
        result = self.stringtointegerobj.myAtoi("2147483648")
        expected = 2147483647
        self.assertEqual(result, expected)

    def test_myAtoi_Test08(self):
        result = self.stringtointegerobj.myAtoi("")
        expected = 0
        self.assertEqual(result, expected)

    def test_myAtoi_Test09(self):
        result = self.stringtointegerobj.myAtoi("+")
        expected = 0
        self.assertEqual(result, expected)

    def test_myAtoi_Test10(self):
        result = self.stringtointegerobj.myAtoi("+words 432")
        expected = 0
        self.assertEqual(result, expected)

    def test_main(self):
        result = program8.stringtointeger_main()
        expected = -321
        self.assertEqual(result, expected)