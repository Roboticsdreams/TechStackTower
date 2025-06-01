import unittest

from leetcode.problems import program7


class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.reverseintegerobj = program7.ReverseInteger()

    def test_reverse_Test01(self):
        result = self.reverseintegerobj.reverse(123)
        expected = 321
        self.assertEqual(result, expected)

    def test_reverse_Test02(self):
        result = self.reverseintegerobj.reverse(-123)
        expected = -321
        self.assertEqual(result, expected)

    def test_reverse_Test03(self):
        result = self.reverseintegerobj.reverse(120)
        expected = 21
        self.assertEqual(result, expected)

    def test_reverse_Test04(self):
        result = self.reverseintegerobj.reverse(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_reverse_Test05(self):
        result = self.reverseintegerobj.reverse(1563847412)
        expected = 0
        self.assertEqual(result, expected)

    def test_reverse_Test06(self):
        result = self.reverseintegerobj.reverse(-1563847412)
        expected = 0
        self.assertEqual(result, expected)

    def test_main(self):
        result = program7.reverseinteger_main()
        expected = -123
        self.assertEqual(result, expected)