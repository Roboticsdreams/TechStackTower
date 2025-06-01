import unittest

from leetcode.problems import program6


class TestZigzagConversion(unittest.TestCase):
    def setUp(self):
        self.zigzagobj = program6.ZigzagConversion()

    def test_zigzagConversion_Test01(self):
        result = self.zigzagobj.convert("PAYPALISHIRING",3)
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(result, expected)

    def test_zigzagConversion_Test02(self):
        result = self.zigzagobj.convert("PAYPALISHIRING",4)
        expected = "PINALSIGYAHRPI"
        self.assertEqual(result, expected)

    def test_zigzagConversion_Test03(self):
        result = self.zigzagobj.convert("AB",1)
        expected = "AB"
        self.assertEqual(result, expected)

    def test_main(self):
        result = program6.zigzag_main()
        expected = "PAHNAPLSIIGYIR"
        self.assertEqual(result, expected)