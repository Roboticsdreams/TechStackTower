from typing import List


class MedianSortedArrays:
    """"
    Median of Two Sorted Arrays [Hard]

    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.

    Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

    Example 3:
    Input: nums1 = [0,0], nums2 = [0,0]
    Output: 0.00000

    Example 4:
    Input: nums1 = [], nums2 = [1]
    Output: 1.00000

    Example 5:
    Input: nums1 = [2], nums2 = []
    Output: 2.00000

    Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = nums1
        l2 = nums2
        l3 = []

        i = 0
        j = 0

        while (i < len(l1) and j < len(l2)) :
            if l1[i] < l2[j]:
                l3.append(l1[i])
                i = i + 1
            elif l1[i] > l2[j]:
                l3.append(l2[j])
                j = j + 1
            else:
                l3.append(l1[i])
                l3.append(l2[j])
                i = i + 1
                j = j + 1

        while i < len(l1):
            l3.append(l1[i])
            i = i + 1

        while j < len(l2):
            l3.append(l2[j])
            j = j + 1

        if (len(l3) % 2 == 0):
             return (l3[(len(l3)//2) - 1] + l3[len(l3)//2])/2
        else:
            return l3[len(l3)//2]

def mediansortedarray_main():
    p4 = MedianSortedArrays()
    return p4.findMedianSortedArrays([1,3],[2])