import unittest

from leetcode.problems import program4


class TestMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.mediansortedarrayobj = program4.MedianSortedArrays()

    def test_findMedianSortedArrays_Test01(self):
        result = self.mediansortedarrayobj.findMedianSortedArrays([1,3],[2])
        expected = 2.00000
        self.assertEqual(result, expected)

    def test_findMedianSortedArrays_Test02(self):
        result = self.mediansortedarrayobj.findMedianSortedArrays([1,3],[2,4])
        expected = 2.50000
        self.assertEqual(result, expected)

    def test_findMedianSortedArrays_Test03(self):
        result = self.mediansortedarrayobj.findMedianSortedArrays([0,0],[0,0])
        expected = 0.00000
        self.assertEqual(result, expected)

    def test_findMedianSortedArrays_Test04(self):
        result = self.mediansortedarrayobj.findMedianSortedArrays([],[1])
        expected = 1.00000
        self.assertEqual(result, expected)

    def test_findMedianSortedArrays_Test05(self):
        result = self.mediansortedarrayobj.findMedianSortedArrays([2],[])
        expected = 2.00000
        self.assertEqual(result, expected)

    def test_main(self):
        result = program4.mediansortedarray_main()
        expected = 2.00000
        self.assertEqual(result, expected)
