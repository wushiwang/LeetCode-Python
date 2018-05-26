#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.26%)
# Total Accepted:    263.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
#


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) == 0 and len(nums2) == 0:
            return 0.0
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return nums1[len(nums1) // 2] * 1.0 if len(nums1) % 2 == 1\
                else (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2

        # pre-condition: len(nums1) >= len(nums2)
        # result belong to [L, R + 1)
        # O(lg(m+n))

        n = len(nums1) + len(nums2)

        # All elements in nums1
        if len(nums1) >= n // 2 + 1:
            if nums1[n // 2] <= nums2[0]:
                return nums1[n // 2] * 1.0 if n % 2 == 1\
                    else (nums1[n // 2] + nums1[n // 2 - 1]) / 2

        # Elements in nums1 and nums2
        L, R = 0, n // 2
        while L < R:
            M = (L + R) // 2
            i1 = n // 2 - M - 1
            if i1 < 0:
                R = M
            elif i1 >= len(nums2):
                L = M + 1
            else:
                a0, a1 = nums1[M], nums2[i1]
                if a0 <= a1:
                    if M + 1 == len(nums1) or nums1[M + 1] >= a1:
                        return a1 * 1.0 if n % 2 == 1 else ((max(nums2[i1 - 1], a0) if i1 != 0 else a0) + a1) / 2
                    else:
                        L = M + 1
                elif a0 > a1:
                    if i1 + 1 == len(nums2) or a0 <= nums2[i1 + 1]:
                        return a0 * 1.0 if n % 2 == 1 else (a0 + (max(nums1[M - 1], a1) if M != 0 else a1)) / 2
                    else:
                        R = M

