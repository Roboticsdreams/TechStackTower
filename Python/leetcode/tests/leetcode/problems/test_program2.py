import unittest

from leetcode.problems import program2


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.add2numsobj = program2.AddTwoNumbers()

    def test_addtwonumbers_Test01(self):
        arraylist1 = [2,4,3]
        arraylist2 = [5,6,4]
        expected = [7,0,8]
        l1 = self.add2numsobj.arraytolink(arraylist1)
        l2 = self.add2numsobj.arraytolink(arraylist2)
        l3 = self.add2numsobj.addtwonumbers(l1, l2)
        result = self.add2numsobj.linktoarray(l3)
        self.assertEqual(result, expected)

    def test_addtwonumbers_Test02(self):
        arraylist1 = [0]
        arraylist2 = [0]
        expected = [0]
        l1 = self.add2numsobj.arraytolink(arraylist1)
        l2 = self.add2numsobj.arraytolink(arraylist2)
        l3 = self.add2numsobj.addtwonumbers(l1, l2)
        result = self.add2numsobj.linktoarray(l3)
        self.assertEqual(result, expected)

    def test_addtwonumbers_Test03(self):
        arraylist1 = [9,9,9,9,9,9,9]
        arraylist2 = [9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        l1 = self.add2numsobj.arraytolink(arraylist1)
        l2 = self.add2numsobj.arraytolink(arraylist2)
        l3 = self.add2numsobj.addtwonumbers(l1, l2)
        result = self.add2numsobj.linktoarray(l3)
        self.assertEqual(result, expected)

    def test_addtwonumbers_Test04(self):
        arraylist1 = [9,9,9,9]
        arraylist2 = [9,9,9,9,9,9,9]
        expected = [8,9,9,9,0,0,0,1]
        l1 = self.add2numsobj.arraytolink(arraylist1)
        l2 = self.add2numsobj.arraytolink(arraylist2)
        l3 = self.add2numsobj.addtwonumbers(l1, l2)
        result = self.add2numsobj.linktoarray(l3)
        self.assertEqual(result, expected)

    def test_main(self):
        result = program2.addtwonumbers_main()
        expected = [4, 4, 4]
        self.assertEqual(result, expected)
