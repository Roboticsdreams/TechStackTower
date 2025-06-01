import unittest

from leetcode.problems import program1


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.twosumobj = program1.TwoSum()

    def test_twosum_Test01(self):
        listinput = [2, 7, 11, 15]
        result = self.twosumobj.twosum(9, listinput)
        expected = [0, 1]
        self.assertEqual(result, expected)

    def test_twosum_Test02(self):
        listinput = [3, 2, 4]
        result = self.twosumobj.twosum(6, listinput)
        expected = [1, 2]
        self.assertEqual(result, expected)

    def test_twosum_Test03(self):
        listinput = [3, 3]
        result = self.twosumobj.twosum(6, listinput)
        expected = [0, 1]
        self.assertEqual(result, expected)

    def test_twosum_Test04(self):
        listinput = [3, 5]
        result = self.twosumobj.twosum(6, listinput)
        expected = []
        self.assertEqual(result, expected)

    def test_main(self):
        result = program1.twosum_main()
        expected = [0, 1]
        self.assertEqual(result, expected)
