#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (48.55%)
# Total Accepted:    140.6K
# Total Submissions: 289.5K
# Testcase Example:  '[]\n[]'
#
#
# Given two arrays, write a function to compute their intersection.
#
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].
#
#
# Note:
#
# Each element in the result must be unique.
# The result can be in any order.
#


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = set(nums1), set(nums2)
        res = []
        for n in nums1:
            if n in nums2:
                res.append(n)
        return res
