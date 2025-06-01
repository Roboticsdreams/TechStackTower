import unittest

from tests.leetcode.problems.test_program1 import TestTwoSum
from tests.leetcode.problems.test_program2 import TestAddTwoNumbers
from tests.leetcode.problems.test_program3 import TestLongestSubstring
from tests.leetcode.problems.test_program4 import TestMedianSortedArrays
from tests.leetcode.problems.test_program5 import TestLongestPalindrome
from tests.leetcode.problems.test_program6 import TestZigzagConversion
from tests.leetcode.problems.test_program7 import TestReverseInteger
from tests.leetcode.problems.test_program8 import TestStringtoInteger
from tests.leetcode.problems.test_program9 import TestPalindromeNumber

def suite():
    suites = unittest.TestSuite()
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestTwoSum))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAddTwoNumbers))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLongestSubstring))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestMedianSortedArrays))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLongestPalindrome))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestZigzagConversion))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestReverseInteger))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStringtoInteger))
    suites.addTest(unittest.TestLoader().loadTestsFromTestCase(TestPalindromeNumber))
    return suites


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())